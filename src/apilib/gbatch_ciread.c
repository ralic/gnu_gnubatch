/* gbatch_ciread.c -- API routine to read command interpreter list

   Copyright 2009 Free Software Foundation, Inc.

   This program is free software: you can redistribute it and/or modify
   it under the terms of the GNU General Public License as published by
   the Free Software Foundation, either version 3 of the License, or
   (at your option) any later version.

   This program is distributed in the hope that it will be useful,
   but WITHOUT ANY WARRANTY; without even the implied warranty of
   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
   GNU General Public License for more details.

   You should have received a copy of the GNU General Public License
   along with this program.  If not, see <http://www.gnu.org/licenses/>.  */

#include <stdio.h>
#include <sys/types.h>
#include "gbatch.h"
#include "xbapi_int.h"
#include "incl_net.h"
#include "incl_unix.h"

extern int  gbatch_read(const int, char *, unsigned);
extern int  gbatch_rmsg(const struct api_fd *, struct api_msg *);
extern int  gbatch_wmsg(const struct api_fd *, struct api_msg *);
extern struct api_fd *gbatch_look_fd(const int);

int     gbatch_ciread(const int fd, const unsigned flags, int *nci, Cmdint **cis)
{
        int             ret;
        unsigned        numcis;
#ifndef WORDS_BIGENDIAN
        unsigned        cnt;
        Cmdint          *cilist;
#endif
        struct  api_fd  *fdp = gbatch_look_fd(fd);
        struct  api_msg msg;

        if  (!fdp)
                return  XB_INVALID_FD;
        msg.code = API_CIREAD;
        msg.un.lister.flags = htonl(flags);
        if  ((ret = gbatch_wmsg(fdp, &msg)))
                return  ret;
        if  ((ret = gbatch_rmsg(fdp, &msg)))
                return  ret;
        if  (msg.retcode != 0)
                return  (SHORT) ntohs(msg.retcode);

        /* Get number of cis */

        numcis = ntohl(msg.un.r_lister.nitems);
        if  (nci)
                *nci = (int) numcis;

        /* Try to allocate enough space to hold the list.  If we don't
           succeed we'd better carry on reading it so we don't
           get out of sync.  */

        if  (numcis != 0)  {
                unsigned  nbytes = numcis * sizeof(Cmdint);
                if  (nbytes > fdp->bufmax)  {
                        if  (fdp->bufmax != 0)  {
                                free(fdp->buff);
                                fdp->bufmax = 0;
                                fdp->buff = (char *) 0;
                        }
                        if  (!(fdp->buff = malloc(nbytes)))  {
                                unsigned  cnt;
                                for  (cnt = 0;  cnt < numcis;  cnt++)  {
                                        Cmdint  slurp;
                                        if  ((ret = gbatch_read(fdp->sockfd, (char *) &slurp, sizeof(slurp))))
                                                return  ret;
                                }
                                return  XB_NOMEM;
                        }
                        fdp->bufmax = nbytes;
                }

                if  ((ret = gbatch_read(fdp->sockfd, fdp->buff, nbytes)))
                        return  ret;

#ifndef WORDS_BIGENDIAN
                cilist = (Cmdint *) fdp->buff;
                for  (cnt = 0;  cnt < numcis;  cilist++, cnt++)
                        cilist->ci_ll = ntohs(cilist->ci_ll);
#endif
        }

        /* Set up answer */

        if  (cis)
                *cis = (Cmdint *) fdp->buff;
        return  XB_OK;
}
