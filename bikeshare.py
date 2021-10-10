{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Explore Bike Share Data\n",
    "\n",
    "For this project, your goal is to ask and answer three questions about the available bikeshare data from Washington, Chicago, and New York.  This notebook can be submitted directly through the workspace when you are confident in your results.\n",
    "\n",
    "You will be graded against the project [Rubric](https://review.udacity.com/#!/rubrics/2508/view) by a mentor after you have submitted.  To get you started, you can use the template below, but feel free to be creative in your solutions!"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "ny = read.csv('new_york_city.csv')\n",
    "wash = read.csv('washington.csv')\n",
    "chi = read.csv('chicago.csv')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
           "<table>\n",
           "<thead><tr><th scope=col>X</th><th scope=col>Start.Time</th><th scope=col>End.Time</th><th scope=col>Trip.Duration</th><th scope=col>Start.Station</th><th scope=col>End.Station</th><th scope=col>User.Type</th><th scope=col>Gender</th><th scope=col>Birth.Year</th></tr></thead>\n",
           "<tbody>\n",
           "\t<tr><td>5688089                                       </td><td>2017-06-11 14:55:05                           </td><td>2017-06-11 15:08:21                           </td><td> 795                                          </td><td>Suffolk St &amp; Stanton St                   </td><td>W Broadway &amp; Spring St                    </td><td>Subscriber                                    </td><td><span style=white-space:pre-wrap>Male  </span></td><td>1998                                          </td></tr>\n",
           "\t<tr><td>4096714                                                           </td><td>2017-05-11 15:30:11                                               </td><td>2017-05-11 15:41:43                                               </td><td> 692                                                              </td><td>Lexington Ave &amp; E 63 St                                       </td><td><span style=white-space:pre-wrap>1 Ave &amp; E 78 St       </span></td><td>Subscriber                                                        </td><td><span style=white-space:pre-wrap>Male  </span>                    </td><td>1981                                                              </td></tr>\n",
           "\t<tr><td>2173887                                                            </td><td>2017-03-29 13:26:26                                                </td><td>2017-03-29 13:48:31                                                </td><td>1325                                                               </td><td><span style=white-space:pre-wrap>1 Pl &amp; Clinton St      </span></td><td><span style=white-space:pre-wrap>Henry St &amp; Degraw St  </span> </td><td>Subscriber                                                         </td><td><span style=white-space:pre-wrap>Male  </span>                     </td><td>1987                                                               </td></tr>\n",
           "\t<tr><td>3945638                                                            </td><td>2017-05-08 19:47:18                                                </td><td>2017-05-08 19:59:01                                                </td><td> 703                                                               </td><td><span style=white-space:pre-wrap>Barrow St &amp; Hudson St  </span></td><td><span style=white-space:pre-wrap>W 20 St &amp; 8 Ave       </span> </td><td>Subscriber                                                         </td><td>Female                                                             </td><td>1986                                                               </td></tr>\n",
           "\t<tr><td>6208972                                                            </td><td>2017-06-21 07:49:16                                                </td><td>2017-06-21 07:54:46                                                </td><td> 329                                                               </td><td><span style=white-space:pre-wrap>1 Ave &amp; E 44 St        </span></td><td><span style=white-space:pre-wrap>E 53 St &amp; 3 Ave       </span> </td><td>Subscriber                                                         </td><td><span style=white-space:pre-wrap>Male  </span>                     </td><td>1992                                                               </td></tr>\n",
           "\t<tr><td>1285652                                                            </td><td>2017-02-22 18:55:24                                                </td><td>2017-02-22 19:12:03                                                </td><td> 998                                                               </td><td><span style=white-space:pre-wrap>State St &amp; Smith St    </span></td><td><span style=white-space:pre-wrap>Bond St &amp; Fulton St   </span> </td><td>Subscriber                                                         </td><td><span style=white-space:pre-wrap>Male  </span>                     </td><td>1986                                                               </td></tr>\n",
           "</tbody>\n",
           "</table>\n"
      ],
      "text/latex": [
           "\\begin{tabular}{r|lllllllll}\n",
           " X & Start.Time & End.Time & Trip.Duration & Start.Station & End.Station & User.Type & Gender & Birth.Year\\\\\n",
           "\\hline\n",
           "\t 5688089                   & 2017-06-11 14:55:05       & 2017-06-11 15:08:21       &  795                      & Suffolk St \\& Stanton St & W Broadway \\& Spring St  & Subscriber                & Male                      & 1998                     \\\\\n",
           "\t 4096714                   & 2017-05-11 15:30:11       & 2017-05-11 15:41:43       &  692                      & Lexington Ave \\& E 63 St & 1 Ave \\& E 78 St         & Subscriber                & Male                      & 1981                     \\\\\n",
           "\t 2173887                   & 2017-03-29 13:26:26       & 2017-03-29 13:48:31       & 1325                      & 1 Pl \\& Clinton St       & Henry St \\& Degraw St    & Subscriber                & Male                      & 1987                     \\\\\n",
           "\t 3945638                   & 2017-05-08 19:47:18       & 2017-05-08 19:59:01       &  703                      & Barrow St \\& Hudson St   & W 20 St \\& 8 Ave         & Subscriber                & Female                    & 1986                     \\\\\n",
           "\t 6208972                   & 2017-06-21 07:49:16       & 2017-06-21 07:54:46       &  329                      & 1 Ave \\& E 44 St         & E 53 St \\& 3 Ave         & Subscriber                & Male                      & 1992                     \\\\\n",
           "\t 1285652                   & 2017-02-22 18:55:24       & 2017-02-22 19:12:03       &  998                      & State St \\& Smith St     & Bond St \\& Fulton St     & Subscriber                & Male                      & 1986                     \\\\\n",
           "\\end{tabular}\n"
      ],
      "text/markdown": [
       "\n",
       "| X | Start.Time | End.Time | Trip.Duration | Start.Station | End.Station | User.Type | Gender | Birth.Year |\n",
       "|---|---|---|---|---|---|---|---|---|\n",
       "| 5688089                 | 2017-06-11 14:55:05     | 2017-06-11 15:08:21     |  795                    | Suffolk St & Stanton St | W Broadway & Spring St  | Subscriber              | Male                    | 1998                    |\n",
       "| 4096714                 | 2017-05-11 15:30:11     | 2017-05-11 15:41:43     |  692                    | Lexington Ave & E 63 St | 1 Ave & E 78 St         | Subscriber              | Male                    | 1981                    |\n",
       "| 2173887                 | 2017-03-29 13:26:26     | 2017-03-29 13:48:31     | 1325                    | 1 Pl & Clinton St       | Henry St & Degraw St    | Subscriber              | Male                    | 1987                    |\n",
       "| 3945638                 | 2017-05-08 19:47:18     | 2017-05-08 19:59:01     |  703                    | Barrow St & Hudson St   | W 20 St & 8 Ave         | Subscriber              | Female                  | 1986                    |\n",
       "| 6208972                 | 2017-06-21 07:49:16     | 2017-06-21 07:54:46     |  329                    | 1 Ave & E 44 St         | E 53 St & 3 Ave         | Subscriber              | Male                    | 1992                    |\n",
       "| 1285652                 | 2017-02-22 18:55:24     | 2017-02-22 19:12:03     |  998                    | State St & Smith St     | Bond St & Fulton St     | Subscriber              | Male                    | 1986                    |\n",
       "\n"
      ],
      "text/plain": [
       "  X       Start.Time          End.Time            Trip.Duration\n",
       "1 5688089 2017-06-11 14:55:05 2017-06-11 15:08:21  795         \n",
       "2 4096714 2017-05-11 15:30:11 2017-05-11 15:41:43  692         \n",
       "3 2173887 2017-03-29 13:26:26 2017-03-29 13:48:31 1325         \n",
       "4 3945638 2017-05-08 19:47:18 2017-05-08 19:59:01  703         \n",
       "5 6208972 2017-06-21 07:49:16 2017-06-21 07:54:46  329         \n",
       "6 1285652 2017-02-22 18:55:24 2017-02-22 19:12:03  998         \n",
       "  Start.Station           End.Station            User.Type  Gender Birth.Year\n",
       "1 Suffolk St & Stanton St W Broadway & Spring St Subscriber Male   1998      \n",
       "2 Lexington Ave & E 63 St 1 Ave & E 78 St        Subscriber Male   1981      \n",
       "3 1 Pl & Clinton St       Henry St & Degraw St   Subscriber Male   1987      \n",
       "4 Barrow St & Hudson St   W 20 St & 8 Ave        Subscriber Female 1986      \n",
       "5 1 Ave & E 44 St         E 53 St & 3 Ave        Subscriber Male   1992      \n",
       "6 State St & Smith St     Bond St & Fulton St    Subscriber Male   1986      "
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "head(ny)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<table>\n",
       "<thead><tr><th scope=col>X</th><th scope=col>Start.Time</th><th scope=col>End.Time</th><th scope=col>Trip.Duration</th><th scope=col>Start.Station</th><th scope=col>End.Station</th><th scope=col>User.Type</th></tr></thead>\n",
       "<tbody>\n",
       "\t<tr><td>1621326                                                                                        </td><td>2017-06-21 08:36:34                                                                            </td><td>2017-06-21 08:44:43                                                                            </td><td> 489.066                                                                                       </td><td><span style=white-space:pre-wrap>14th &amp; Belmont St NW                       </span>        </td><td><span style=white-space:pre-wrap>15th &amp; K St NW                                     </span></td><td>Subscriber                                                                                     </td></tr>\n",
       "\t<tr><td> 482740                                                                                        </td><td>2017-03-11 10:40:00                                                                            </td><td>2017-03-11 10:46:00                                                                            </td><td> 402.549                                                                                       </td><td><span style=white-space:pre-wrap>Yuma St &amp; Tenley Circle NW                 </span>        </td><td><span style=white-space:pre-wrap>Connecticut Ave &amp; Yuma St NW                       </span></td><td>Subscriber                                                                                     </td></tr>\n",
       "\t<tr><td>1330037                                                                                        </td><td>2017-05-30 01:02:59                                                                            </td><td>2017-05-30 01:13:37                                                                            </td><td> 637.251                                                                                       </td><td><span style=white-space:pre-wrap>17th St &amp; Massachusetts Ave NW             </span>        </td><td><span style=white-space:pre-wrap>5th &amp; K St NW                                      </span></td><td>Subscriber                                                                                     </td></tr>\n",
       "\t<tr><td> 665458                                                                                        </td><td>2017-04-02 07:48:35                                                                            </td><td>2017-04-02 08:19:03                                                                            </td><td>1827.341                                                                                       </td><td><span style=white-space:pre-wrap>Constitution Ave &amp; 2nd St NW/DOL           </span>        </td><td><span style=white-space:pre-wrap>M St &amp; Pennsylvania Ave NW                         </span></td><td><span style=white-space:pre-wrap>Customer  </span>                                             </td></tr>\n",
       "\t<tr><td>1481135                                                                                        </td><td>2017-06-10 08:36:28                                                                            </td><td>2017-06-10 09:02:17                                                                            </td><td>1549.427                                                                                       </td><td>Henry Bacon Dr &amp; Lincoln Memorial Circle NW                                                </td><td><span style=white-space:pre-wrap>Maine Ave &amp; 7th St SW                              </span></td><td>Subscriber                                                                                     </td></tr>\n",
       "\t<tr><td>1148202                                                                                </td><td>2017-05-14 07:18:18                                                                    </td><td>2017-05-14 07:24:56                                                                    </td><td> 398.000                                                                               </td><td><span style=white-space:pre-wrap>1st &amp; K St SE                              </span></td><td>Eastern Market Metro / Pennsylvania Ave &amp; 7th St SE                                </td><td>Subscriber                                                                             </td></tr>\n",
       "</tbody>\n",
       "</table>\n"
      ],
      "text/latex": [
       "\\begin{tabular}{r|lllllll}\n",
       " X & Start.Time & End.Time & Trip.Duration & Start.Station & End.Station & User.Type\\\\\n",
       "\\hline\n",
       "\t 1621326                                               & 2017-06-21 08:36:34                                   & 2017-06-21 08:44:43                                   &  489.066                                              & 14th \\& Belmont St NW                                & 15th \\& K St NW                                      & Subscriber                                           \\\\\n",
       "\t  482740                                               & 2017-03-11 10:40:00                                   & 2017-03-11 10:46:00                                   &  402.549                                              & Yuma St \\& Tenley Circle NW                          & Connecticut Ave \\& Yuma St NW                        & Subscriber                                           \\\\\n",
       "\t 1330037                                               & 2017-05-30 01:02:59                                   & 2017-05-30 01:13:37                                   &  637.251                                              & 17th St \\& Massachusetts Ave NW                      & 5th \\& K St NW                                       & Subscriber                                           \\\\\n",
       "\t  665458                                               & 2017-04-02 07:48:35                                   & 2017-04-02 08:19:03                                   & 1827.341                                              & Constitution Ave \\& 2nd St NW/DOL                    & M St \\& Pennsylvania Ave NW                          & Customer                                             \\\\\n",
       "\t 1481135                                               & 2017-06-10 08:36:28                                   & 2017-06-10 09:02:17                                   & 1549.427                                              & Henry Bacon Dr \\& Lincoln Memorial Circle NW         & Maine Ave \\& 7th St SW                               & Subscriber                                           \\\\\n",
       "\t 1148202                                               & 2017-05-14 07:18:18                                   & 2017-05-14 07:24:56                                   &  398.000                                              & 1st \\& K St SE                                       & Eastern Market Metro / Pennsylvania Ave \\& 7th St SE & Subscriber                                           \\\\\n",
       "\\end{tabular}\n"
      ],
      "text/markdown": [
       "\n",
       "| X | Start.Time | End.Time | Trip.Duration | Start.Station | End.Station | User.Type |\n",
       "|---|---|---|---|---|---|---|\n",
       "| 1621326                                             | 2017-06-21 08:36:34                                 | 2017-06-21 08:44:43                                 |  489.066                                            | 14th & Belmont St NW                                | 15th & K St NW                                      | Subscriber                                          |\n",
       "|  482740                                             | 2017-03-11 10:40:00                                 | 2017-03-11 10:46:00                                 |  402.549                                            | Yuma St & Tenley Circle NW                          | Connecticut Ave & Yuma St NW                        | Subscriber                                          |\n",
       "| 1330037                                             | 2017-05-30 01:02:59                                 | 2017-05-30 01:13:37                                 |  637.251                                            | 17th St & Massachusetts Ave NW                      | 5th & K St NW                                       | Subscriber                                          |\n",
       "|  665458                                             | 2017-04-02 07:48:35                                 | 2017-04-02 08:19:03                                 | 1827.341                                            | Constitution Ave & 2nd St NW/DOL                    | M St & Pennsylvania Ave NW                          | Customer                                            |\n",
       "| 1481135                                             | 2017-06-10 08:36:28                                 | 2017-06-10 09:02:17                                 | 1549.427                                            | Henry Bacon Dr & Lincoln Memorial Circle NW         | Maine Ave & 7th St SW                               | Subscriber                                          |\n",
       "| 1148202                                             | 2017-05-14 07:18:18                                 | 2017-05-14 07:24:56                                 |  398.000                                            | 1st & K St SE                                       | Eastern Market Metro / Pennsylvania Ave & 7th St SE | Subscriber                                          |\n",
       "\n"
      ],
      "text/plain": [
       "  X       Start.Time          End.Time            Trip.Duration\n",
       "1 1621326 2017-06-21 08:36:34 2017-06-21 08:44:43  489.066     \n",
       "2  482740 2017-03-11 10:40:00 2017-03-11 10:46:00  402.549     \n",
       "3 1330037 2017-05-30 01:02:59 2017-05-30 01:13:37  637.251     \n",
       "4  665458 2017-04-02 07:48:35 2017-04-02 08:19:03 1827.341     \n",
       "5 1481135 2017-06-10 08:36:28 2017-06-10 09:02:17 1549.427     \n",
       "6 1148202 2017-05-14 07:18:18 2017-05-14 07:24:56  398.000     \n",
       "  Start.Station                              \n",
       "1 14th & Belmont St NW                       \n",
       "2 Yuma St & Tenley Circle NW                 \n",
       "3 17th St & Massachusetts Ave NW             \n",
       "4 Constitution Ave & 2nd St NW/DOL           \n",
       "5 Henry Bacon Dr & Lincoln Memorial Circle NW\n",
       "6 1st & K St SE                              \n",
       "  End.Station                                         User.Type \n",
       "1 15th & K St NW                                      Subscriber\n",
       "2 Connecticut Ave & Yuma St NW                        Subscriber\n",
       "3 5th & K St NW                                       Subscriber\n",
       "4 M St & Pennsylvania Ave NW                          Customer  \n",
       "5 Maine Ave & 7th St SW                               Subscriber\n",
       "6 Eastern Market Metro / Pennsylvania Ave & 7th St SE Subscriber"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "head(wash)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<table>\n",
       "<thead><tr><th></th><th scope=col>X</th><th scope=col>Start.Time</th><th scope=col>End.Time</th><th scope=col>Trip.Duration</th><th scope=col>Start.Station</th><th scope=col>End.Station</th><th scope=col>User.Type</th><th scope=col>Gender</th><th scope=col>Birth.Year</th></tr></thead>\n",
       "<tbody>\n",
       "\t<tr><th scope=row>8625</th><td> 397518                         </td><td>2017-03-24 16:52:16             </td><td>2017-03-24 16:57:57             </td><td> 341                            </td><td>Southport Ave &amp; Waveland Ave</td><td>Southport Ave &amp; Waveland Ave</td><td>Subscriber                      </td><td>Male                            </td><td>1990                            </td></tr>\n",
       "\t<tr><th scope=row>8626</th><td> 879494                                                                 </td><td>2017-05-18 05:06:50                                                     </td><td>2017-05-18 05:22:10                                                     </td><td> 920                                                                    </td><td><span style=white-space:pre-wrap>Artesian Ave &amp; Hubbard St   </span></td><td><span style=white-space:pre-wrap>Wacker Dr &amp; Washington St   </span></td><td>Subscriber                                                              </td><td>Male                                                                    </td><td>1959                                                                    </td></tr>\n",
       "\t<tr><th scope=row>8627</th><td> 360389                                                                 </td><td>2017-03-19 07:21:29                                                     </td><td>2017-03-19 07:27:18                                                     </td><td> 349                                                                    </td><td><span style=white-space:pre-wrap>Wabash Ave &amp; Roosevelt Rd   </span></td><td><span style=white-space:pre-wrap>Wells St &amp; Polk St          </span></td><td>Subscriber                                                              </td><td>Male                                                                    </td><td>1987                                                                    </td></tr>\n",
       "\t<tr><th scope=row>8628</th><td> 858496                                                                 </td><td>2017-05-16 17:03:24                                                     </td><td>2017-05-16 17:31:12                                                     </td><td>1668                                                                    </td><td><span style=white-space:pre-wrap>Ashland Ave &amp; Harrison St   </span></td><td><span style=white-space:pre-wrap>Wells St &amp; Concord Ln       </span></td><td>Subscriber                                                              </td><td>Male                                                                    </td><td>1963                                                                    </td></tr>\n",
       "\t<tr><th scope=row>8629</th><td> 777620                                                                 </td><td>2017-05-10 08:53:03                                                     </td><td>2017-05-10 08:54:32                                                     </td><td><span style=white-space:pre-wrap>  89</span>                            </td><td><span style=white-space:pre-wrap>Western Ave &amp; Leland Ave    </span></td><td><span style=white-space:pre-wrap>Western Ave &amp; Leland Ave    </span></td><td>Subscriber                                                              </td><td>Male                                                                    </td><td>1977                                                                    </td></tr>\n",
       "\t<tr><th scope=row>8630</th><td>1230561                     </td><td>2017-06-11 14:52:13         </td><td>2017-06-11 15:42:33         </td><td>3020                        </td><td>Waba                        </td><td>                            </td><td>                            </td><td>                            </td><td>  NA                        </td></tr>\n",
       "</tbody>\n",
       "</table>\n"
      ],
      "text/latex": [
       "\\begin{tabular}{r|lllllllll}\n",
       "  & X & Start.Time & End.Time & Trip.Duration & Start.Station & End.Station & User.Type & Gender & Birth.Year\\\\\n",
       "\\hline\n",
       "\t8625 &  397518                        & 2017-03-24 16:52:16            & 2017-03-24 16:57:57            &  341                           & Southport Ave \\& Waveland Ave & Southport Ave \\& Waveland Ave & Subscriber                     & Male                           & 1990                          \\\\\n",
       "\t8626 &  879494                        & 2017-05-18 05:06:50            & 2017-05-18 05:22:10            &  920                           & Artesian Ave \\& Hubbard St    & Wacker Dr \\& Washington St    & Subscriber                     & Male                           & 1959                          \\\\\n",
       "\t8627 &  360389                        & 2017-03-19 07:21:29            & 2017-03-19 07:27:18            &  349                           & Wabash Ave \\& Roosevelt Rd    & Wells St \\& Polk St           & Subscriber                     & Male                           & 1987                          \\\\\n",
       "\t8628 &  858496                        & 2017-05-16 17:03:24            & 2017-05-16 17:31:12            & 1668                           & Ashland Ave \\& Harrison St    & Wells St \\& Concord Ln        & Subscriber                     & Male                           & 1963                          \\\\\n",
       "\t8629 &  777620                        & 2017-05-10 08:53:03            & 2017-05-10 08:54:32            &   89                           & Western Ave \\& Leland Ave     & Western Ave \\& Leland Ave     & Subscriber                     & Male                           & 1977                          \\\\\n",
       "\t8630 & 1230561                      & 2017-06-11 14:52:13          & 2017-06-11 15:42:33          & 3020                         & Waba                         &                              &                              &                              &   NA                        \\\\\n",
       "\\end{tabular}\n"
      ],
      "text/markdown": [
       "\n",
       "| <!--/--> | X | Start.Time | End.Time | Trip.Duration | Start.Station | End.Station | User.Type | Gender | Birth.Year |\n",
       "|---|---|---|---|---|---|---|---|---|---|\n",
       "| 8625 |  397518                      | 2017-03-24 16:52:16          | 2017-03-24 16:57:57          |  341                         | Southport Ave & Waveland Ave | Southport Ave & Waveland Ave | Subscriber                   | Male                         | 1990                         |\n",
       "| 8626 |  879494                      | 2017-05-18 05:06:50          | 2017-05-18 05:22:10          |  920                         | Artesian Ave & Hubbard St    | Wacker Dr & Washington St    | Subscriber                   | Male                         | 1959                         |\n",
       "| 8627 |  360389                      | 2017-03-19 07:21:29          | 2017-03-19 07:27:18          |  349                         | Wabash Ave & Roosevelt Rd    | Wells St & Polk St           | Subscriber                   | Male                         | 1987                         |\n",
       "| 8628 |  858496                      | 2017-05-16 17:03:24          | 2017-05-16 17:31:12          | 1668                         | Ashland Ave & Harrison St    | Wells St & Concord Ln        | Subscriber                   | Male                         | 1963                         |\n",
       "| 8629 |  777620                      | 2017-05-10 08:53:03          | 2017-05-10 08:54:32          |   89                         | Western Ave & Leland Ave     | Western Ave & Leland Ave     | Subscriber                   | Male                         | 1977                         |\n",
       "| 8630 | 1230561                      | 2017-06-11 14:52:13          | 2017-06-11 15:42:33          | 3020                         | Waba                         |                              |                              |                              |   NA                         |\n",
       "\n"
      ],
      "text/plain": [
       "     X       Start.Time          End.Time            Trip.Duration\n",
       "8625  397518 2017-03-24 16:52:16 2017-03-24 16:57:57  341         \n",
       "8626  879494 2017-05-18 05:06:50 2017-05-18 05:22:10  920         \n",
       "8627  360389 2017-03-19 07:21:29 2017-03-19 07:27:18  349         \n",
       "8628  858496 2017-05-16 17:03:24 2017-05-16 17:31:12 1668         \n",
       "8629  777620 2017-05-10 08:53:03 2017-05-10 08:54:32   89         \n",
       "8630 1230561 2017-06-11 14:52:13 2017-06-11 15:42:33 3020         \n",
       "     Start.Station                End.Station                  User.Type \n",
       "8625 Southport Ave & Waveland Ave Southport Ave & Waveland Ave Subscriber\n",
       "8626 Artesian Ave & Hubbard St    Wacker Dr & Washington St    Subscriber\n",
       "8627 Wabash Ave & Roosevelt Rd    Wells St & Polk St           Subscriber\n",
       "8628 Ashland Ave & Harrison St    Wells St & Concord Ln        Subscriber\n",
       "8629 Western Ave & Leland Ave     Western Ave & Leland Ave     Subscriber\n",
       "8630 Waba                                                                \n",
       "     Gender Birth.Year\n",
       "8625 Male   1990      \n",
       "8626 Male   1959      \n",
       "8627 Male   1987      \n",
       "8628 Male   1963      \n",
       "8629 Male   1977      \n",
       "8630          NA      "
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "tail(chi)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### What is the most common month?\n",
    "\n",
    "**June is more popular.**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<ol class=list-inline>\n",
       "\t<li>'X'</li>\n",
       "\t<li>'Start.Time'</li>\n",
       "\t<li>'End.Time'</li>\n",
       "\t<li>'Trip.Duration'</li>\n",
       "\t<li>'Start.Station'</li>\n",
       "\t<li>'End.Station'</li>\n",
       "\t<li>'User.Type'</li>\n",
       "</ol>\n"
      ],
      "text/latex": [
       "\\begin{enumerate*}\n",
       "\\item 'X'\n",
       "\\item 'Start.Time'\n",
       "\\item 'End.Time'\n",
       "\\item 'Trip.Duration'\n",
       "\\item 'Start.Station'\n",
       "\\item 'End.Station'\n",
       "\\item 'User.Type'\n",
       "\\end{enumerate*}\n"
      ],
      "text/markdown": [
       "1. 'X'\n",
       "2. 'Start.Time'\n",
       "3. 'End.Time'\n",
       "4. 'Trip.Duration'\n",
       "5. 'Start.Station'\n",
       "6. 'End.Station'\n",
       "7. 'User.Type'\n",
       "\n",
       "\n"
      ],
      "text/plain": [
       "[1] \"X\"             \"Start.Time\"    \"End.Time\"      \"Trip.Duration\"\n",
       "[5] \"Start.Station\" \"End.Station\"   \"User.Type\"    "
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/html": [
       "<ol class=list-inline>\n",
       "\t<li>'X'</li>\n",
       "\t<li>'Start.Time'</li>\n",
       "\t<li>'End.Time'</li>\n",
       "\t<li>'Trip.Duration'</li>\n",
       "\t<li>'Start.Station'</li>\n",
       "\t<li>'End.Station'</li>\n",
       "\t<li>'User.Type'</li>\n",
       "\t<li>'Gender'</li>\n",
       "\t<li>'Birth.Year'</li>\n",
       "</ol>\n"
      ],
      "text/latex": [
       "\\begin{enumerate*}\n",
       "\\item 'X'\n",
       "\\item 'Start.Time'\n",
       "\\item 'End.Time'\n",
       "\\item 'Trip.Duration'\n",
       "\\item 'Start.Station'\n",
       "\\item 'End.Station'\n",
       "\\item 'User.Type'\n",
       "\\item 'Gender'\n",
       "\\item 'Birth.Year'\n",
       "\\end{enumerate*}\n"
      ],
      "text/markdown": [
       "1. 'X'\n",
       "2. 'Start.Time'\n",
       "3. 'End.Time'\n",
       "4. 'Trip.Duration'\n",
       "5. 'Start.Station'\n",
       "6. 'End.Station'\n",
       "7. 'User.Type'\n",
       "8. 'Gender'\n",
       "9. 'Birth.Year'\n",
       "\n",
       "\n"
      ],
      "text/plain": [
       "[1] \"X\"             \"Start.Time\"    \"End.Time\"      \"Trip.Duration\"\n",
       "[5] \"Start.Station\" \"End.Station\"   \"User.Type\"     \"Gender\"       \n",
       "[9] \"Birth.Year\"   "
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/html": [
       "<ol class=list-inline>\n",
       "\t<li>'X'</li>\n",
       "\t<li>'Start.Time'</li>\n",
       "\t<li>'End.Time'</li>\n",
       "\t<li>'Trip.Duration'</li>\n",
       "\t<li>'Start.Station'</li>\n",
       "\t<li>'End.Station'</li>\n",
       "\t<li>'User.Type'</li>\n",
       "\t<li>'Gender'</li>\n",
       "\t<li>'Birth.Year'</li>\n",
       "</ol>\n"
      ],
      "text/latex": [
       "\\begin{enumerate*}\n",
       "\\item 'X'\n",
       "\\item 'Start.Time'\n",
       "\\item 'End.Time'\n",
       "\\item 'Trip.Duration'\n",
       "\\item 'Start.Station'\n",
       "\\item 'End.Station'\n",
       "\\item 'User.Type'\n",
       "\\item 'Gender'\n",
       "\\item 'Birth.Year'\n",
       "\\end{enumerate*}\n"
      ],
      "text/markdown": [
       "1. 'X'\n",
       "2. 'Start.Time'\n",
       "3. 'End.Time'\n",
       "4. 'Trip.Duration'\n",
       "5. 'Start.Station'\n",
       "6. 'End.Station'\n",
       "7. 'User.Type'\n",
       "8. 'Gender'\n",
       "9. 'Birth.Year'\n",
       "\n",
       "\n"
      ],
      "text/plain": [
       "[1] \"X\"             \"Start.Time\"    \"End.Time\"      \"Trip.Duration\"\n",
       "[5] \"Start.Station\" \"End.Station\"   \"User.Type\"     \"Gender\"       \n",
       "[9] \"Birth.Year\"   "
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "# First let us join the 3 documents (add gender and year column to WDC)\n",
    "\n",
    "names(wash)\n",
    "names(ny)\n",
    "names(chi)\n",
    "wash$Gender <- \" \"\n",
    "wash$Birth.Year <- \" \"\n",
    "\n",
    "dt <- rbind(wash, ny, chi)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<ol class=list-inline>\n",
       "\t<li>'06'</li>\n",
       "\t<li>'03'</li>\n",
       "\t<li>'05'</li>\n",
       "\t<li>'04'</li>\n",
       "\t<li>'06'</li>\n",
       "\t<li>'05'</li>\n",
       "</ol>\n"
      ],
      "text/latex": [
       "\\begin{enumerate*}\n",
       "\\item '06'\n",
       "\\item '03'\n",
       "\\item '05'\n",
       "\\item '04'\n",
       "\\item '06'\n",
       "\\item '05'\n",
       "\\end{enumerate*}\n"
      ],
      "text/markdown": [
       "1. '06'\n",
       "2. '03'\n",
       "3. '05'\n",
       "4. '04'\n",
       "5. '06'\n",
       "6. '05'\n",
       "\n",
       "\n"
      ],
      "text/plain": [
       "[1] \"06\" \"03\" \"05\" \"04\" \"06\" \"05\""
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/plain": [
       "\n",
       "         01    02    03    04    05    06 \n",
       "    1 15341 18857 19235 30709 31157 37151 "
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/html": [
       "<ol class=list-inline>\n",
       "\t<li>'2017'</li>\n",
       "\t<li>'2017'</li>\n",
       "\t<li>'2017'</li>\n",
       "\t<li>'2017'</li>\n",
       "\t<li>'2017'</li>\n",
       "\t<li>'2017'</li>\n",
       "</ol>\n"
      ],
      "text/latex": [
       "\\begin{enumerate*}\n",
       "\\item '2017'\n",
       "\\item '2017'\n",
       "\\item '2017'\n",
       "\\item '2017'\n",
       "\\item '2017'\n",
       "\\item '2017'\n",
       "\\end{enumerate*}\n"
      ],
      "text/markdown": [
       "1. '2017'\n",
       "2. '2017'\n",
       "3. '2017'\n",
       "4. '2017'\n",
       "5. '2017'\n",
       "6. '2017'\n",
       "\n",
       "\n"
      ],
      "text/plain": [
       "[1] \"2017\" \"2017\" \"2017\" \"2017\" \"2017\" \"2017\""
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/plain": [
       "\n",
       "         2017 \n",
       "     1 152450 "
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/html": [
       "'character'"
      ],
      "text/latex": [
       "'character'"
      ],
      "text/markdown": [
       "'character'"
      ],
      "text/plain": [
       "[1] \"character\""
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/html": [
       "'numeric'"
      ],
      "text/latex": [
       "'numeric'"
      ],
      "text/markdown": [
       "'numeric'"
      ],
      "text/plain": [
       "[1] \"numeric\""
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "dt$month <- substr(dt$Start.Time, 6, 7) \n",
    "dt$year <- substr(dt$Start.Time, 1, 4) \n",
    "head(dt$month)\n",
    "table(dt$month)\n",
    "head(dt$year)\n",
    "table(dt$year) ###table shows Junes was the popular month with 37,151 times\n",
    "\n",
    "library(ggplot2)\n",
    "class(dt$month)\n",
    "dt$month <- as.numeric(dt$month)\n",
    "class(dt$month)\n",
    "###June is more popular"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "Warning message:\n",
      "“Removed 1 rows containing non-finite values (stat_bin).”"
     ]
    },
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAA0gAAANICAIAAAByhViMAAAACXBIWXMAABJ0AAASdAHeZh94\nAAAgAElEQVR4nOzdeXyU9b3o8WdmspMQIgEEsYpIAa1itS6IIlZrr0JV6tX2qLgcKtJWqcdq\n64IXiz3WVlG0tVqwWK4eu91DkWrr3rq0LujRYt1FpYhSDUICJCHb3D/mnty8AiSTZTLJL+/3\nX5lnZvJ8n5knw4eZZ2ZiyWQyAgCg74tnewAAALqHsAMACISwAwAIhLADAAiEsAMACISwAwAI\nhLADAAiEsGvfZZddFovFbr/99mwP0me89NJLhxxySF5eXnFx8Zo1a7I9Tlvmzp0bi8V+8pOf\nZGsAe1f6MndnvfTSS7FYbMqUKamT6dwpra7SaT2zA9jNml133XWxWOyGG27I9iCQKf0x7FKP\nyHvvvffOLlBcXByLxdavX586WVZWtscee5SUlKS/irvuumvFihVdHbTPmjFjxsqVK4844ohZ\ns2YVFRVtf4HUXRCLxa6++uod/oYpU6a0vAtC0mrf6MTeRaZ1152SzuNAz+wA/Xk36+ePxvRD\n/THsOuq73/3ue++9d8YZZ6R/le985zv99qFk27Ztf//73wcOHPjQQw/deOONQ4YMaePCP/jB\nD1599dUem603aLVvdGLvItO6605J53GgZ3aA/ryb9edHY/onYdf93nnnnSCfakpTTU1NFEVl\nZWU5OTltX3L//fevq6s777zz+s/32vXzfaNfcV/3Bu4F+iFh177tD0/5P//n/3z+85/fZZdd\n8vLyRowYcfzxx//xj39MnfU//+f/HD16dBRFP//5z2Ox2BFHHJFaXl9ff/PNNx988MElJSUF\nBQV77733BRdc8MEHH7Rc0T/+8Y/TTz99yJAhRUVFBx988LJlyz755JNYLHbooYemLnDllVfG\nYrEVK1b89Kc/3W233QYNGpRaXlVVdfnll48fP76wsDA/P3/MmDGXXnppVVVV82++6qqrUld8\n+umnp0yZUlJSMmTIkHPOOWfz5s3JZHLhwoXjxo0rKiraZ599fvCDH7SdWW1vyMknn1xWVhZF\n0Zo1a1Ivtr799ts7+1VHHHHEaaed9te//rXdQ38uuOCCWCz2i1/8ouXCZ555JhaLTZs2revb\nGI/H//SnPx111FEDBw4sLi4+4ogjHnnkkZYXSCaTd9xxx8SJE0tKSgoLC8ePH3/VVVdt3bq1\n+QI7u2ta2uG+0Wrv6vRWtDth1OZ+u0MXX3xxLBZbtmxZ6sYpLS0tKSmZPHnyo48+2qEbJ0pj\n/09zXa2ks+rtrVmz5qtf/Wp5eXlRUdEBBxywZMmSVhfY/k++3au0ssP7eoc7Sat1pXk7dPSu\n3Nlu9sorr0yfPn3o0KEFBQUHHHDAL3/5y7a3q92Hmu11epdud59pdyt29mgcRVEikXj11Ven\nTZtWVlZWWFh4wAEH/PrXv25726GvaOc5Fba3ePHiWbNmDRky5LTTThs6dOi6deuWL18+derU\npUuXzpgx49xzzy0pKfnFL35x2GGHfeUrX9ltt92iKGpqajrppJP++Mc/jhs3bubMmQMHDnz+\n+edvvfXWZcuWPf3003vssUcURRs2bDjiiCPWrl07adKkY4899v333z/jjDPmzp0bRVFBQUFq\n1Xl5eVEUPf7447fffvtJJ51UXFwcRVF9ff20adOefPLJgw466IILLqivr3/ggQduuOGGxx9/\n/Omnn04kEs1XfOaZZ2677bYvfvGLZ5999r333rt06dKmpqYRI0bcc889U6dOra6u/tWvfnXF\nFVeMHDlyxowZO9z2djdk5syZhx566BVXXFFWVva//tf/iqKojZdia2trb7nllocffviyyy47\n8cQTU7dVp3VlG1966aWLL7746KOPPu+881avXr1ixYrjjz/+kUceOeqoo1IXOOuss+6+++7h\nw4eff/75+fn5jz322Pe///377rvviSeeSB23tMO7ppUd7hvdtRXtTtj2ftvGTfqnP/3p5z//\n+Re+8IXzzjvv7bffXrFixRe/+MVHHnmk+X0D7a46nf0/zXW10u6qt7dx48Yjjzxy7dq1kydP\nnjx58scff3zllVcef/zxO7xwp6+yw/s6nZ0knduhE3flDtfy4osvnnXWWYceeuiZZ5755ptv\n3n///aeffvqwYcM+//nP7/Ba6TzU7GxdHd2l099n2tiKNv7i1q1bN2nSpEMOOWTmzJlvvfXW\nihUr/uVf/qW8vPyYY45J5waEXi3Z/7z44otRFI0ePXpnFxgwYEAURR9++GHq5He/+90oim67\n7bbUyf322y+Korfffrv58mvXri0pKTnssMNSJ3/7299GUTRz5szmCyxatCiKookTJ9bW1jYv\nTEXbaaedljp55ZVXRlF06qmnNl/gL3/5S2FhYRRFRx11VGrJtddeG0VRaWnpgw8+2Hyx//zP\n/4yi6LDDDmtoaEgt2bZt27hx46IoWrFiRWrJD37wgyiK8vPz//SnP6WWrFmzJpFI5Obmjhs3\nbsOGDamFd9xxRxRF06ZN29ktk86GbNy4MYqiPfbYY2e/JPnfd8E555zT/DtPPvnklhdIFVXz\nXfDNb34ziqI777yz5WWefvrpKIqmTp3alW1M3ezxePzee+9t/s3XX399FEWTJk1KnUz9V/6g\ngw6qqqpKLWlqarrggguiKLrssstSS3Z412xv+32j1d7Vua1IZ8J299vtNd84v//971vdOM3X\nSmfV6e//ba8rdZkf//jH6a96e6n/b3zlK19pXvLhhx/uuuuuLf/QWt0p6Vxle9vf1zvcSVqt\nK53boRN35Q53s7y8vLvuuqv5MpdcckkURWefffbOfkk6DzXb69wunc4+k85WbH8v7PBa3/nO\nd6IoOuuss3a2FdCH9N+XYj/44INjd6K2traNK27atCkWi6XiL2XkyJEVFRWpztihpUuXRlF0\n1VVX5efnNy+89NJL8/Lyli9fnjoo7fe//31qYfMFDj/88K9+9astf08sFouiaPz48ccdd1zz\nwgMPPHDZsmU//vGPm//HnJeXd9JJJ0VRtGrVqpZXnzJlSvMzH5/61Kf222+/+vr6Cy+8cJdd\ndkktTL2suXr16q5sSPqSyWQURV/72tcmT568fPnyZcuWdejqO9S5bTzkkENOPPHE5pMXXHBB\nQUHBX//6108++SSKosWLF0dR9IMf/KD5SaBYLHbNNdfk5uambpBoJ3dNj21FOhN2Yr9NmThx\nYvPr3VEUXXjhhUVFRc8++2z6N076u03b62olnVVv7957742i6KKLLmpesuuuu379619v4xbo\nxFV2KP2dpO3bodN3ZSsHH3zwmWee2Xzy1FNPjaLozTff3Nnl03+o2V5Hd+n095mObkXKYYcd\n1vJa06dPj6Kol382E6Sp/4ZdTU3NozvR2NjYxhW/9KUvJZPJo48+esmSJc2H5aZeFNihZDL5\nwgsvRFF0+OGHt1w+cODAsWPH1tXVvfLKK01NTa+//no8Hj/ggANaXmbq1Knb/8KJEye2PLnn\nnntOnz79c5/7XBRFmzdvXr9+/fr161MfMtKqtFr98oEDB0ZRtP/++7dasrM+S2dDdnwTtCkW\niy1atCg/P/+CCy6orKzsxG9oqXPb2PLgmyiKCgoKxo0bl0wm33jjjSiKnnnmmWi7rR40aNBn\nPvOZDz/88B//+EfzwlZ3TY9tRToTdnS/bTZp0qSWJ/Pz8/fee+9kMvn++++ns+oO7TZtr6uV\n9O+XZk1NTa+99loURRMmTGi5vPkw1m65StvS2Unavh06fVe2cthhh7U8mTo6to3/nqX/ULO9\nDu3SHdpnOroVO7xWqi+7/vgDvUH/PcZu9OjROzuuv7i4uI3jrxcuXNjY2LhkyZKZM2dGUbTP\nPvtMmzZt9uzZo0aN2uHlt2zZUltbm5eXV1pa2uqs1PFnFRUVW7ZsqaurKy0tzc3NbXmB1KEk\nO7xWS8uXL7/hhhteeOGFtp9rLC8vb3ky9fxBy4WpJcmdvHkinQ1pY+1tGDt27BVXXDFv3rzv\nfve7XfwM1c5t4/Dhw1v9ntQD/caNG2tqarZs2RJF0Q6PiIqiaN26dZ/61KdSP7f92S7p69BW\npDlhR/fbZsOGDWu1JPVv5z//+c90Vl1WVpb+btPGulot79D90iz1h1ZQUJA6yKHZ4MGDd/hL\nOneVtqWzk7R9O3T6rmwl9Wpys7b//FPSfKjZXod26Q491HRiK6Lt7oV4PJ7OtaBP6L9h12m5\nubm33377vHnzVqxY8cc//vGxxx770Y9+tHDhwrvuuuu0007b/vJtPNA0NTWlLpA6N3XJ7a+7\n/QAtTy5atOj8888vKSmZPXv2IYccUlpaGo/Hly9f/rOf/ayzm7hj6WxIp3/5ZZdd9utf/3rR\nokVnnHHGkUce2enf0znbH/ed2pZ4PJ76IRaLpQ602l7Lf1da3TU9I80JO7rfNkv9m9dSah9I\nJBLprLpDu00b62q1vEP3S6vftv0wbTxJ34mrtC2dnaTt26HTd2UXhfFQA8ETdp2UeiPe+eef\nX1tb+4tf/OLCCy88//zzTzrppJZHhKQUFxcXFRVVV1dv2rSp1adgfPzxx1EUDRkypLi4OJFI\nbN68ubGxseW/YWvXrm13kvnz50dRdN99902ePLl5YUePtklHOhvS6V+el5e3aNGiI488ctas\nWS+99FKrf8h3+ED/4Ycfdnp1rWz/XOOGDRuiKNpll10KCgpKS0srKyu/+c1vdtcTct2rQxOm\nv982S90ULW3atCmKomHDhqW56vR3mzbW1Wp55+6X1B/atm3bampqWj4D18ZHnXXiKl2Xzu3Q\nibuyi8J4qIHg9d9j7DptzZo1LZOioKBg9uzZhx9++KZNm955550dXiV1VMpf/vKXlgs/+eST\nN954o7CwcN99900kEqNGjWpsbHz99ddbXuaBBx5oe5ht27atW7euuLi45UNtMpls94qd0+6G\ndOWXT5o0adasWa+//vq1117b6mWv1Ae+pN5v22zlypVdWV1Lzz77bMuT27Zte+ONN+LxeOod\nf6mjqZ544olW19rhEf1Zkc6EndhvU5577rmWJzdv3vz6668nEondd989zVWnv9u0va5WOnG/\nJBKJMWPGRNsd7P/UU09141W6ru3bodN3ZVeE9FADYRN2HfO3v/1tzz33PPPMM+vq6poXbt68\n+Z133kkkEkOHDo3+u0Ja/p87dSjMtdde2/Ja1157bUNDwxlnnJH6H/YXv/jFKIp+/OMfN1/g\nueeeu+eee9qeJz8/f5dddtmyZUvzc3vJZHL+/PmpI8dT/8vvRulsSFf88Ic/HD58+HXXXbdu\n3bqWy/faa6/ovz9SIbXktddeS70psls8+uijf/3rX5tPLl68uKam5uijj04d0J3a6quvvjr1\nbEHKk08+OWzYsNRb8NK3/b7RLdqdMJ39dmceffTR1NsUUn7xi1/U1dVNnjw5/Rsn/d2m7XV1\ndKt36IQTToii6MYbb2xe8u677/785z9v4xboxFWirt3XbdwOXbkru6KPPtRk6C8OejMvxXbM\nhAkTTj/99HvuuWf8+PHHH3/84MGDKyoq7r///vfff/9b3/pW6njq8ePHx2Kx+++/f+bMmXl5\nebfddtuMGTOWLVt27733HnTQQccff3xubu6zzz776KOPfvrTn77uuutSv/mSSy65++67f/az\nn61Zs+aQQw5Zs2bNsmXL5s6dm/oAqjacc845N9544zHHHHP22WdHUXTfffdt3Lhx6dKlX/zi\nF3/1q1/tvvvu3fgFkelsSFeUlpbecsstp5566ksvvdRy+SmnnHLZZZc9/vjjkyZNOuywwz78\n8MP77rtv3rx5l156aeqYm05raGiIomjmzJnHH3/89OnT99prr9dee+23v/1tfn7+v//7v6cu\nc9pppy1fvvyXv/zlZz/72a985SslJSV///vfV6xYUVhY2PLjadKx/b7RleGbtTthOvvtzpx5\n5pnHHXfcl7/85b333vutt976j//4j9zc3NRHsqWz6qgju03b6+roVu/Qt7/97f/9v//3b37z\nm3feeWfixIkff/zxH//4x/POO++GG27oxqtEXbuv27gdunJXdlE6DzUjR47slnV110NNhv7i\noFfL6Kfk9U5d/IDixsbGW2+99fDDDy8vL08kEqWlpUceeeSSJUuampqaf8N1111XXl6en59/\n4IEHppbU19cvXLjwwAMPLCoqys/PHzdu3OWXX75x48ZWg33hC18oKSkZOHDgUUcd9dhjj738\n8stRFE2ZMiV1gdRHa15//fUtr1VTU3PllVeOHj06Pz9/9913/8Y3vlFRUZFMJs8555wBAwbs\nuuuuq1at2uEVUx8C/Nprr7X8VVF7ny3c7oak/wHFO/so1OaPlGu+C5LJ5Msvv/z5z3++qKio\nuLj40EMPXb58eep5mrZvnHa3MfXhZL/97W//9Kc/TZ48ubi4eMCAAUcdddSTTz7Z8vc0NjYu\nXrw49dVVOTk5I0eOPOuss1r+2h2ufYda7Rs7/OTYTtxT7U6Yzn7bSurDcn/605+mvoSjuLi4\nuLj4qKOOeuKJJzp04yTT2G3SWVerDyhOc9Xbe+2110466aRBgwYVFBTst99+ixcvTj2jc+ih\nh6Yu0OpOSecqO9Tqvt7hnbvDDyhu+3boxF2Zzm721ltvRVE0YcKEnf2SdB5qtr9Wp3fpdveZ\nNLcinXuh3W2HPqQ/hl0fkno5pvnLFaAnbR9SYayrN3M7AF3kGLve4p///Ocf/vCHVgdop57Z\n6ujHUwEA/ZOw6y0efvjhqVOnfv3rX6+vr08tqaysXLBgQfTfX7YDANA2b57oLU477bSf/exn\nTz311Gc/+9kTTjihurr63nvvff/996dPn556wywAQNs8Y9db5OXl/eEPf/je974XRdFtt922\nZMmS8vLy66+//je/+U22RwMA+ob/92VWAAD0dZ6xAwAIhLADAAiEsAMACISwAwAIhLADAAiE\nsAMACISwAwAIhLADAAhEv/tKscrKykyvIicnJxaLNX/la29WVFSUTCZramqyPUj78vPzGxoa\nGhsbsz1IO+LxeGFhYUNDw7Zt27I9S/sKCwtra2t7/6eU5+Tk5Ofnb9u2raGhIduztCMWixUU\nFPSVv6mcnJyampqmpqZsz9KORCKRk5PTV/6mYrFYdXV1tgdpX25ubjKZ7BN/U0VFRY2NjbW1\ntdmepX0FBQV1dXU98DdVWlq6s7P6Xdj1QG8lEom+EnY5OTlNTU19YtT8/Pw+MWrqX6CGhobe\nP2oURcXFxfX19b0/7FK3am1tbe+/VWOx2IABA3r/nNF/h12f+P9SFEU5OTl94lYtLi6Ox+N9\nYtRU2PX+UWOxWE5OTp8YNYqiwsLCxsbG7Oayl2IBAAIh7AAAAiHsAAACIewAAAIh7AAAAiHs\nAAACIewAAAIh7AAAAiHsAAACIewAAAIh7AAAAiHsAAACIewAAAIh7AAAAiHsAAACIewAAAIh\n7AAAAiHsAAACIewAAAIh7AAAAiHsAAACIewAAAIh7AAAAiHsAAACIewAAAIh7AAAAiHsAAAC\nIewAAAIh7AAAAiHsAAACIewAAAKRk+0BAICedssttzz33HONjY3ZHqQdsVgsLy+vqampvr4+\n27O0Lzc391//9V8POeSQLM4g7ACg3/nhD3+4adOmbE8RoIKCAmEHAPSoZDK5V3nOfRfsmu1B\nwvFORf20n/wzmUxmdwxhBwD9UW4iNqpcBnSbusYsJ12KN08AAARC2AEABELYAQAEQtgBAARC\n2AEABELYAQAEQtgBAARC2AEABELYAQAEQtgBAARC2AEABELYAQAEQtgBAARC2AEABELYAQAE\nQtgBAARC2AEABELYAQAEQtgBAARC2AEABELYAQAEQtgBAARC2AEABELYAQAEQtgBAARC2AEA\nBELYAQAEQtgBAARC2AEABELYAQAEQtgBAARC2AEABELYAQAEQtgBAARC2AEABELYAQAEIifb\nA/S0srKyTK8iFotFUZSfn5/pFXVdLBaLx+M9cJt0XTwez8vLSyaT2R6kHc33fm5ubrZnaV88\nHh80aFC2p2hf6lYtKioqLCzM9iztSyQSfeVvKoqi0tLSPvFnFYvF+srfVCwW6xM7QOrPim6X\nm5ub6R2gqampjXP7Xdht3Lgx06soKCiIx+PV1dWZXlHXDR48uKmpqQduk64rLi6uq6urq6vL\n9iDtSP2jvm3bti1btmR7lvaVlZVt2rSp9/+7XlBQUFxcXF1dXVtbm+1Z2hGLxQYNGtRX/qYK\nCgoqKysbGxuzPUs7cnNz8/Pz+8rfVDwe7xM7QO//w++j6uvre2AHKC8v39lZXooFAAiEsAMA\nCISwAwAIhLADAAiEsAMACISwAwAIhLADAAiEsAMACISwAwAIhLADAAiEsAMACISwAwAIhLAD\nAAiEsAMACISwAwAIhLADAAiEsAMACISwAwAIhLADAAiEsAMACISwAwAIhLADAAiEsAMACISw\nAwAIhLADAAiEsAMACISwAwAIhLADAAiEsAMACISwAwAIhLADAAiEsAMACISwAwAIhLADAAiE\nsAMACISwAwAIhLADAAiEsAMACISwAwAIhLADAAiEsAMACISwAwAIhLADAAiEsAMACISwAwAI\nhLADAAiEsAMACISwAwAIhLADAAiEsAMACISwAwAIhLADAAiEsAMACISwAwAIhLADAAiEsAMA\nCISwAwAIhLADAAiEsAMACISwAwAIhLADAAiEsAMACISwAwAIhLADAAiEsAMACISwAwAIhLAD\nAAhETrYHAIC2NDQ0fPDBB9XV1dkepH0bN26Mx+ObNm3K9iDta2pqyvYIZISwA6BXu+iii+6+\n++5sTxGiotxsT0D3E3YA9Grr16+PouhL+xflJmLZniUcy17cmu0RyAhhB0AfsGhG+aBCx4V3\nm6ILhV2Y/JEAAARC2AEABELYAQAEQtgBAARC2AEABMK7YgG6zUMPPXThhRc2NjZme5C0xGKx\nZDKZ7Snat3Wr929CuoQdQLd56aWXNmzYMHpI7sBCn7jWbV7e3JDtEaDPEHYA3WzBqbt8cZ/C\nbE8Rjt0vW1uxpW88CQpZ5xg7AIBACDsAgEAIOwCAQAg7AIBACDsAgEAIOwCAQPTEx52sXbt2\n6dKlr732WjKZHDVq1IwZM8aNGxdF0ZYtWxYtWrRq1ar6+vqxY8fOnj176NCh3bgcAKBfyfgz\ndg0NDVddddWAAQN+9KMfLViwYMiQId/73vdqamqiKFq4cOFHH300b96866+/vqioaP78+U1N\nTd24HACgX8l42G3duvWkk06aPXv2brvtNnz48FNPPXXr1q0ffvhhRUXFypUrZ82aNWrUqBEj\nRsyePXvdunUvv/xydy3P9HYBAPQ2GX8ptrS0dPr06amfN2/evGLFipEjR+6+++7PP/98bm7u\nqFGjUmcVFxePHDnyjTfeqK6u7pblEyZMyPSmAQD0Kj30lWJNTU2nnnpqfX39Zz7zmWuuuSY3\nN7eqqqqkpCQW+/9fp1haWlpZWVlaWtoty5tPzp0794EHHkj9XFZW9vDDD2dwO1soKirqmRV1\nUSKRKC8vz/YUaSkoKMj2COkqKCjoK9MOHjw42yOkq7i4uLi4ONtTtKOv/OEDGZKXl5fpf1Ub\nG9v6hr0eCrt4PH7zzTdv3Ljx/vvvv+KKKxYsWBBFUcsaa6m7lqeMGDFi/PjxqZ9LSkoaGjL+\nZdLxeDyKoj5xnF9OTk4ymWx7F+kl4vF4MplMJpPZHqQdsVgskUg0NTX1iR0gkUj0lXs/Ho/3\niVu1908IZFQymcx0aTQ1NSUSiZ2d20NhF0XRyJEjR44cue+++55++umPP/54eXl5VVVVMpls\nzrLKysqysrJBgwZ1y/Lm9X7jG9/4xje+0XyyoqIi01taUFAQj8erq6szvaKuGzx4cFNT06ZN\nm7I9SPuKi4vr6urq6uqyPUg7EolEWVlZXV3dli1bsj1L+8rKyiorK3t/LhcUFBQXF1dXV9fW\n1mZ7lnb0/gmBjKqvr++Bf1XbeFIw42+eePHFF2fNmrVt27bUyVgslpOTE0XRmDFj6uvrV69e\nnVpeVVW1du3a8ePHd9fyTG8XAEBvk/GwGzNmTG1t7cKFC9euXbt+/fo77rijtrb2oIMO2mWX\nXSZOnHjrrbe+++6769atu+mmm0aPHr3PPvt01/JMbxcAQG+T8Zdii4uLr7nmmjvvvPPb3/52\nLBb71Kc+ddVVV+26665RFM2ZM2fRokVXX311Y2PjvvvuO3fu3NTLqd21HACgX+mJY+z22GOP\nq6++evvlRUVFF110UeaWAwD0K74rFgAgEMIOACAQwg4AIBDCDgAgEMIOACAQwg4AIBDCDgAg\nEMIOACAQwg4AIBDCDgAgEMIOACAQwg4AIBDCDgAgEMIOACAQwg4AIBDCDgAgEMIOACAQwg4A\nIBDCDgAgEMIOACAQwg4AIBDCDgAgEMIOACAQwg4AIBDCDgAgEMIOACAQwg4AIBDCDgAgEMIO\nACAQwg4AIBDCDgAgEMIOACAQwg4AIBDCDgAgEMIOACAQwg4AIBDCDgAgEMIOACAQwg4AIBDC\nDgAgEMIOACAQwg4AIBDCDgAgEMIOACAQwg4AIBDCDgAgEMIOACAQwg4AIBDCDgAgEMIOACAQ\nwg4AIBDCDgAgEMIOACAQwg4AIBDCDgAgEMIOACAQwg4AIBDCDgAgEMIOACAQwg4AIBDCDgAg\nEMIOACAQwg4AIBDCDgAgEMIOACAQwg4AIBDCDgAgEMIOACAQwg4AIBDCDgAgEMIOACAQwg4A\nIBDCDgAgEMIOACAQwg4AIBDCDgAgEMIOACAQwg4AIBDCDgAgEMIOACAQwg4AIBDCDgAgEMIO\nACAQwg4AIBA52R6gp+XkZHyT4/F4PB7vgRV1lz4xal+5VROJRBRFfWLUlJycnGQyme0p2hGP\nx6M+cqumRgX6rVgslulHqrYftHv7o2S3GzBgQKZXkXpkT/0D38vFYrF4PN4Dt2OYF6YAACAA\nSURBVEnXJRKJeDze+xMkFotFUZSTk9MnbtV4PF5UVJTtKdqX+pvKz8/Pzc3N9izt6P0TAhmV\nSCQy/fjf1NTUxrn9LuwqKyszvYqCgoJ4PF5dXZ3pFXXd4MGDm5qaeuA26bri4uK6urq6urps\nD9KORCJRVlZWV1e3ZcuWbM/SvrKysqqqqt6fywUFBcXFxTU1NbW1tdmepR3btm3L9ghANjU0\nNPTAv6r5+fk7O8urBgAAgRB2AACBEHYAAIEQdgAAgRB2AACBEHYAAIEQdgAAgRB2AACBEHYA\nAIEQdgAAgRB2AACBEHYAAIEQdgAAgRB2AACBEHYAAIEQdgAAgRB2AACBEHYAAIEQdgAAgRB2\nAACBEHYAAIEQdgAAgRB2AACBEHYAAIEQdgAAgRB2AACBEHYAAIEQdgAAgRB2AACBEHYAAIEQ\ndgAAgRB2AACBEHYAAIEQdgAAgRB2AACBEHYAAIEQdgAAgRB2AACBEHYAAIEQdgAAgRB2AACB\nEHYAAIEQdgAAgRB2AACBEHYAAIEQdgAAgRB2AACBEHYAAIEQdgAAgRB2AACByEnzctXV1ZWV\nlcOHD4+iqKam5te//vWGDRumT5++1157ZXI8AADSldYzdq+//vqoUaOWLl0aRVFDQ8PkyZPP\nPffcSy655MADD3zxxRczPCEAAGlJK+yuvPLKYcOGnXrqqVEU/epXv3r++ed/+tOfvv322/vu\nu++1116b4QkBAEhLWmH31FNPXXbZZaNHj46iaNmyZZ/5zGe+/vWvjx49+pvf/Oazzz6b4QkB\nAEhLWmG3adOm1NF1jY2Nf/7zn0844YTU8iFDhvzzn//M4HQAAKQtrbAbNmzYO++8E0XRY489\ntnHjxv/xP/5HavnatWsHDx6cwekAAEhbWu+KPe644+bOnfv222//8pe/HD169OTJk6Mo+uij\nj26++eZJkyZleEIAANKSVthdc801r7zyynXXXVdeXv773/8+kUhEUTRnzpw1a9bcddddGZ4Q\nAIC0pBV2w4cPf/rpp6uqqgoLC3Nzc1MLL7nkkptvvnnYsGGZHA8AgHSl+wHFURTl5eW99NJL\n77///pFHHlleXn7AAQfk5HTg6gAAZFS6Xym2YMGCoUOHHnLIIV/+8pfffvvtKIrmzZt37rnn\nNjQ0ZHI8AADSlVbYLV68+JJLLjn66KNvv/325oVjx469++67b7rppozNBgBAB6QVdj/5yU9m\nz5597733nn322c0LzzrrrEsvvfSOO+7I2GwAAHRAWmH35ptvnnLKKdsvnzJlyrvvvtvdIwEA\n0Blphd3AgQNra2u3X15ZWVlYWNjdIwEA0Blphd3+++9/ww031NTUtFz4ySefzJ8//7DDDsvM\nYAAAdExan1dy5ZVXHnvssfvvv//UqVOjKFq8ePHtt9/+u9/9rqampuXbKQAAyKK0nrGbMmXK\ngw8+WFJScvPNN0dRtGTJkqVLl44bN+7hhx/2lWIAAL1Eup8wfMwxx/zXf/3XRx999MEHH0RR\ntMcee5SVlWVyMAAAOqZjXx1RWFi45557pn7etGlT6odBgwZ170wAAHRCWmH3zjvvzJkz589/\n/vPWrVu3PzeZTHb3VAAAdFhaYTdz5swXX3zx5JNPHj58eCKRyPRMAAB0Qlpht3Llyoceeujw\nww/P9DQAAHRaWu+KHTBgQPOhdQAA9E5phd2MGTOWLFmS6VEAAOiKtF6Kvfbaa6dOnfrAAw9M\nnDhx8ODBrc697LLLMjAYAAAdk1bY3XjjjY888kgURX/5y1+2P1fYAQD0BmmF3S233HLKKaf8\n27/926677updsQAAvVNaYffJJ5/ccsstI0aMyPQ0AAB0Wlpvnthnn30+/vjjTI8CAEBXpBV2\nCxcuvPjii1etWpXpaQAA6LS0Xoq94oor1qxZM2HChOLi4u3fFfvee+91/1wAAHRQWmEXj8fH\njh07duzYTE8DAECnpRV2TzzxRKbnAACgi9I6xg4AgN6vrWfsxo0bd/bZZ19++eXjxo1r42Kv\nv/562+v45JNPlixZ8re//a2urm6vvfY699xzP/3pT0dRtGXLlkWLFq1ataq+vn7s2LGzZ88e\nOnRoNy4HAOhX2nrGbtCgQYWFhakf2tDuOr7//e9XVFR873vfW7hwYXl5+fz582tra6MoWrhw\n4UcffTRv3rzrr7++qKho/vz5TU1N3bgcAKBfaesZu2eeeabVD52wefPmIUOGnHnmmbvvvnsU\nRWedddbjjz++du3asrKylStX3nTTTaNGjYqiaPbs2TNmzHj55Zd32223blk+YcKETs8MANAX\npfXmic997nN33XXX+PHjWy3/z//8z6uuuurVV19t47olJSWXX35588kNGzbE4/Hy8vLXX389\nNzc3VWNRFBUXF48cOfKNN96orq7uluXNYbd69eoNGzb8v63NyRk9enQ6m9wViUQiHo/n5uZm\nekXdpU+MGo/Hc3JykslktgdpR+o79/rKDhCLxXJzc/vKrZpIJHr/repLF6GfSz2uZnGAtMLu\nhRde2Lp1a6uFDQ0Nr7zyyurVq9Nf2ebNm3/84x+ffPLJZWVlVVVVJSUlsVis+dzS0tLKysrS\n0tJuWd588s4773zggQdSP5eVlT388MPpD9wV+fn5PbOiLkokEqWlpdmeIi15eXnZHiFdeXl5\nfWXagQMHZnuEdBUWFqYODunN+sofPpAhubm5mf5XtbGxsY1z2wm75mA6+OCDd3iBAw88MM05\n3n///WuuueaAAw44++yzW/3yna20i8tTJk+ePGzYsNTPhYWFNTU1aQ7caYlEIhaLNTQ0ZHpF\nXVdYWNjU1LRt27ZsD9K+3NzcxsbG3n/0ZDwez8/Pb2xsrKury/Ys7SsoKEgd8NrLJRKJvLy8\n+vr63v9nVV9fn+0RgGxqbGzMdGk0NTUNGDBgZ+e2E3YvvfTS448//q1vfeukk04qLy9veVYs\nFhsxYsR5552XzhB/+9vffvSjH/3Lv/zLtGnTUksGDRpUVVWVTCabs6yysrKsrKy7ljev+rjj\njjvuuOOaT1ZUVKQzcFcUFBTE4/Hq6upMr6jrCgoKksnk9k/H9kLFxcV1dXW9v5YSiUR+fn59\nfX2fuFXz8vKqq6t7/0uxBQUFeXl527Zt6/0ZKuygn2tsbOyBx//Oh92ECRMmTJjwhz/84frr\nrx8zZkznVv/qq6/+8Ic//Pa3v33QQQc1LxwzZkx9ff3q1av33nvvKIqqqqrWrl07fvz44cOH\nd8vyzo0KANB3pfUBxQ888ECnq66urm7hwoUnnnjiHnvsUfHfamtrd9lll4kTJ956663vvvvu\nunXrbrrpptGjR++zzz7dtbxz0wIA9F1pvXmiK1577bX169ffc88999xzT/PC888/f+rUqXPm\nzFm0aNHVV1/d2Ni47777zp07N/VyanctBwDoVzIedhMmTFixYsUOzyoqKrrooosytxwAoF/x\nXbEAAIFoK+zef//91Fs733vvvd7/bkQAgH6urbAbM2bMY489FkXRqFGjVq1a1VMjAQDQGW0d\nYxeLxX7zm9+kPkD5b3/7284+QeqII47IyGgAAHREW2E3ffr0u+6666677oqi6Gtf+9rOLtb7\nP90UAKA/aCvsli5devrpp1dUVJxzzjnz5s3bc889e2oqAAA6rK2wy8nJmTp1ahRFd9111+mn\nn/7pT3+6p6YCesJzzz334Ycf9v4n3fPy8lJf9Nz738W1Zs2abI8A9GtpfY7dI488EkXRhg0b\nnnnmmQ8++CAej48cOfLwww8vKSnJ8HhApjz//PPHH398tqcAoDulFXZNTU3f+c53brnllpbf\nbz1gwIB58+ZdeumlGZsNyKDNmzdHUTRxr/zDRxdke5Zw/OaFrWs/acj2FED/lVbYLViwYMGC\nBdOnT582bdrw4cObmprWrVu3bNmy73znO8OGDTvrrLMyPSWQIZ8fVzj3hEHZniIcK9/bJuyA\nLEor7O68886LL754wYIFLRfOmjXr/PPPv/nmm4UdAEBvkNZXir3zzjupd1G0ctJJJ7322mvd\nPRIAAJ2RVtjl5OSkvluslfr6+kQi0d0jAQDQGWm9FPvZz372xhtvPO644/Ly8poX1tbW/vSn\nP/3c5z6Xsdng/3v22WfXrFnT0NDbj16Kx+MDBgyor6/f2Te19B5///vfsz0CAN0srbC7/PLL\np02bNmbMmBNOOGG33XZLJpNr1669//77169f/+CDD2Z6RKitrT322GN7f9UBQHalFXYnnHDC\nsmXLLr/88ttvv7154X777bd48eJjjz02Y7PB/1NXV9fQ0DB+19xvHj0w27OE46FXalas2sEh\nFgD0XWmFXRRFJ5988sknn/zBBx+sW7cuFovtvvvuw4YNy+hk0MrIspyZk3wmdrep2NIk7AAC\nk27YpYwYMWLEiBEZGgUAgK5I612xAAD0fsIOACAQwg4AIBDCDgAgEGmF3eGHH/6HP/wh06MA\nANAVaYXd2rVrX3/99UyPAgBAV6QVdrfeeusdd9yxfPny+vr6TA8EAEDnpPU5djfccENOTs70\n6dPz8vLKy8tzc3Nbnvvee+9lZDQAADoirbBramoaMmTIMccck+lpAADotLTC7qmnnsr0HAAA\ndFEHPu6ktrZ25cqVv/vd7yoqKqIoamhoyNhUAAB0WLpht2DBgqFDhx5yyCFf/vKX33777SiK\n5s2bd+6558o7AIBeIq2wW7x48SWXXHL00UfffvvtzQvHjh17991333TTTRmbDQCADkgr7H7y\nk5/Mnj373nvvPfvss5sXnnXWWZdeeukdd9yRsdkAAOiAtMLuzTffPOWUU7ZfPmXKlHfffbe7\nRwIAoDPSCruBAwfW1tZuv7yysrKwsLC7RwIAoDPSCrv999//hhtuqKmpabnwk08+mT9//mGH\nHZaZwQAA6Ji0PsfuyiuvPPbYY/fff/+pU6dGUbR48eLbb7/9d7/7XU1NTcu3UwAAkEVpPWM3\nZcqUBx98sKSk5Oabb46iaMmSJUuXLh03btzDDz88adKkDE8IAEBa0nrGLoqiY4455r/+678+\n+uijDz74IIqiPfbYo6ysLJODAQDQMemGXRRF//jHP1544YWPP/44Ho+vXbv24IMP3nXXXTM3\nGQAAHZJW2G3cuHHGjBn3339/y4XxePyrX/3qokWLBgwYkJnZAADogLTCbs6cOffff/8pp5wy\nbdq01LN069evf/DBB3/5y18WFxf/7Gc/y/CQAAC0L62wu++++771rW8tXLiw5cJzzjln7733\nvu2224QdAEBvkNa7Yrdt23b00Udvv/yoo45q9eF2AABkS1phd9BBB7355pvbL3/77bcPPPDA\n7h4JAIDOSOul2JtvvvnUU08dPXr0l770pdzc3CiKmpqaHn300Ztuuumee+7J8IQAAKSlrbAb\nN25c6odYLFZXV3fKKafk5+ePGDEiHo+vX79+69atI0eOvPDCC//617/2yKgAALSlrbArLy9v\n/nnw4MF77LFH88nUe2Obmpq2bduWueEAAEhfW2H31FNP9dgcAAB0UQe+eSKKos2bNzc2NrZa\nOGjQoO6bBwCATkor7N555505c+b8+c9/3rp16/bnJpPJ7p4KAIAOSyvsZs6c+eKLL5588snD\nhw9PJBKZngkAgE5IK+xWrlz50EMPHX744ZmeBgCATkvrA4oHDBiw5557ZngSAAC6JK2wmzFj\nxpIlSzI9CgAAXZHWS7HXXnvt1KlTH3jggYkTJw4ePLjVuZdddlkGBgMAoGPSCrsbb7zxkUce\niaLoL3/5y/bnCjsAgN4grbC75ZZbTjnllH/7t3/bddddvSsWAKB3SivsPvnkk1tuuWXEiBGZ\nngYAgE5L680T++yzz8cff5zpUQAA6Iq0wm7hwoUXX3zxqlWrMj0NAACdltZLsVdcccWaNWsm\nTJhQXFy8/bti33vvve6fCwCADkor7OLx+NixY8eOHZvpaQAA6LS0wu6JJ57I9BwAAHRRWsfY\nAQDQ+6X1jF15efnOzqqrq6uqquq+eQAA6KS0wu6II45oteTDDz98+eWXR48efdRRR2VgKgAA\nOiytsFu+fPn2C9evX/+Vr3zl+OOP7+6RAADojM4fY7frrrsuWLBg3rx53TgNAACd1qU3T4wc\nOfLVV1/trlEAAOiKzoddMplcsmTJ9p9XDABAVqR1jN0BBxzQakljY+P69esrKiouueSSDEwF\nAECHpRV228vNzd1///1POumk2bNnd+9AAAB0Tlph99JLL2V6DgAAusg3TwAABKKtZ+yOPfbY\ndH7FI4880k3DAADQeW2F3aZNm3a4PBaL5ebmxmKxp59+OplMZmYwAAA6pq2we/7553d21ooV\nK+bMmRNF0bnnntv9QwEA0HEdflfsmjVr5syZs2LFiv333//JJ5+cNGlSJsbq0xoaGtatW1db\nW5vtQdpXWVnZ1NRUVVWV7UHasWXLlmyPAAB9QAfCrr6+/sYbb5w/f34ikViwYMGcOXNycjr5\naSlhO+200x5++OFsTwEA9DvpltkTTzzx9a9//dVXXz311FMXLlw4YsSIjI7Vp/3jH//ITcS+\ntH9RtgcJR3Vd0wOv1GR7CgDo7doPu48//vjSSy9dunTpmDFjHnrooS984Qs9MFZfV5QX+4+Z\nQ7I9RTjWbmz49FXvZ3sKAOjt2vocu2QyuWjRorFjx/7617/+3ve+9/LLL6s6AIBeq61n7CZO\nnPjss8+ecMIJCxcu/NSnPpVMJnf4hoCCgoKMjQcAQLraCrtnn302iqLHHnvs05/+dBsX81F2\nAAC9QVthN2/evB6bo8f0wPOLsVgs06sAAHqheDye6dJo+wm1tsLu6quv7uZZegHVBQBkSCwW\ny25p9LsPoqupyfinZnhtGgD6p8bGxh4ojeLi4p2d1da7YgEA6EOEHQBAIIQdAEAghB0AQCCE\nHQBAIIQdAEAghB0AQCCEHQBAIIQdAEAghB0AQCCEHQBAIIQdAEAghB0AQCCEHQBAIIQdAEAg\nhB0AQCCEHQBAIIQdAEAghB0AQCCEHQBAIIQdAEAghB0AQCCEHQBAIIQdAEAghB0AQCCEHQBA\nIIQdAEAghB0AQCCEHQBAIIQdAEAghB0AQCCEHQBAIIQdAEAghB0AQCCEHQBAIIQdAEAghB0A\nQCCEHQBAIIQdAEAghB0AQCCEHQBAIIQdAEAghB0AQCCEHQBAIIQdAEAghB0AQCCEHQBAIIQd\nAEAghB0AQCCEHQBAIIQdAEAghB0AQCCEHQBAIIQdAEAghB0AQCCEHQBAIIQdAEAghB0AQCCE\nHQBAIIQdAEAghB0AQCCEHQBAIIQdAEAghB0AQCCEHQBAIIQdAEAghB0AQCCEHQBAIIQdAEAg\nhB0AQCCEHQBAIIQdAEAghB0AQCCEHQBAIIQdAEAghB0AQCCEHQBAIIQdAEAghB0AQCCEHQBA\nIIQdAEAghB0AQCCEHQBAIIQdAEAgcnpmNevWrbvpppvefvvt5cuXNy/csmXLokWLVq1aVV9f\nP3bs2NmzZw8dOrQblwMA9Cs98Yzdk08+ecUVV4wcObLV8oULF3700Ufz5s27/vrri4qK5s+f\n39TU1I3LAQD6lZ4Iu/r6+htuuOGwww5rubCiomLlypWzZs0aNWrUiBEjZs+evW7dupdffrm7\nlvfAdgEA9Co98VLs5z//+SiKVq9e3XLhW2+9lZubO2rUqNTJ4uLikSNHvvHGG9XV1d2yfMKE\nCT2waQAAvUcPHWO3vaqqqpKSklgs1ryktLS0srKytLS0W5Y3n3zooYfeeOON1M+FhYVnnHFG\nBrcqiqIoajkMANB/JBKJAQMGZHQVbR9vlrWwi3YeQN21POWJJ5544IEHUj+XlZV97Wtf68iM\nnSHsAKB/SiQShYWFGV1FY2NjG+dmLewGDRpUVVWVTCabM6iysrKsrKy7ljev6Nxzzz3xxBNT\nP+fk5LR8Mi9DkslkplcBAPRC9fX1PVAapaWlOzsra2E3ZsyY+vr61atX77333lEUVVVVrV27\ndvz48cOHD++W5c0rGj169OjRo5tPVlRUZHrThB0A9E/JZLK+vj6LA/TEu2I3btxYUVGxefPm\nKIoqKioqKipqa2t32WWXiRMn3nrrre+++27qU+5Gjx69zz77dNfyHtguAIBepSeesbv00ks/\n+uij1M//+q//GkXR1772tRNPPHHOnDmLFi26+uqrGxsb991337lz56ZeTu2u5QAA/UpPhN0d\nd9yxw+VFRUUXXXRR5pYDAPQrvisWACAQwg4AIBDCDgAgEMIOACAQwg4AIBDCDgAgEMIOACAQ\nwg4AIBDCDgAgEMIOACAQwg4AIBDCDgAgEMIOACAQwg4AIBDCDgAgEMIOACAQwg4AIBDCDgAg\nEMIOACAQwg4AIBDCDgAgEMIOACAQwg4AIBDCDgAgEMIOACAQwg4AIBDCDgAgEMIOACAQwg4A\nIBDCDgAgEMIOACAQwg4AIBDCDgAgEMIOACAQwg4AIBDCDgAgEMIOACAQwg4AIBDCDgAgEMIO\nACAQwg4AIBDCDgAgEMIOACAQwg4AIBDCDgAgEMIOACAQwg4AIBDCDgAgEMIOACAQwg4AIBDC\nDgAgEMIOACAQwg4AIBDCDgAgEMIOACAQwg4AIBDCDgAgEMIOACAQwg4AIBDCDgAgEMIOACAQ\nwg4AIBDCDgAgEMIOACAQwg4AIBDCDgAgEMIOACAQwg4AIBDCDgAgEMIOACAQwg4AIBDCDgAg\nEMIOACAQwg4AIBDCDgAgEMIOACAQwg4AIBDCDgAgEMIOACAQwg4AIBDCDgAgEMIOACAQwg4A\nIBDCDgAgEMIOACAQOdkeoKeVlJRkehWxWCzTqwAAeqGcnJxMl0YymWxrgIyuuxeqqanJ9Cra\nvsUBgFA1NjZmujSSyWRBQcHOzu13YdfQ0JDtEQCAMCWTyeyWhmPsAAACIewAAAIh7AAAAiHs\nAAACIewAAAIh7AAAAiHsAAACIewAAAIh7AAAAiHsAAACIewAAAIh7AAAAiHsAAACIewAAAIh\n7AAAAiHsAAACIewAAAIh7AAAAiHsAAACIewAAAIh7AAAAiHsAAACIewAAAIh7AAAAiHsAAAC\nIewAAAIh7AAAAiHsAAACIewAAAIh7AAAAiHsAAACIewAAAIh7AAAAiHsAAACIewAAAIh7AAA\nAiHsAAACIewAAAIh7AAAAiHsAAACIewAAAIh7AAAAiHsAAACIewAAAIh7AAAAiHsAAACIewA\nAAIh7AAAAiHsAAACIewAAAIh7AAAAiHsAAACIewAAAIh7AAAAiHsAAACIewAAAIh7AAAAiHs\nAAACIewAAAIh7AAAAiHsAAACIewAAAIh7AAAAiHsAAACIewAAAIh7AAAAiHsAAACIewAAAIh\n7AAAAiHsAAACIewAAAIh7AAAAiHsAAACIewAAAIh7AAAAiHsAAACIewAAAIh7AAAAiHsAAAC\nIewAAAIh7AAAAiHsAAACIewAAAIh7AAAApGT7QG6wZYtWxYtWrRq1ar6+vqxY8fOnj176NCh\n2R4KAKCnhfCM3cKFCz/66KN58+Zdf/31RUVF8+fPb2pqyvZQAAA9rc+HXUVFxcqVK2fNmjVq\n1KgRI0bMnj173bp1L7/8crbnAgDoaX0+7N56663c3NxRo0alThYXF48cOfKNN97I7lQAAD2v\nzx9jV1VVVVJSEovFmpeUlpZWVlY2n7zzzjtXrlyZ+rm4uPjf//3fMz1SPB7fuq1p6o//mekV\n9R+1Dckoil74xza3ajd6b0N9FEX3PLfl6dXbsj1LOF5eVxdF0bwVG295tCrbs4SjsqYpiqKv\n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",
      "text/plain": [
       "plot without title"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "ggplot(aes(x = month), data = dt) +\n",
    "    geom_histogram(binwidth = 1, color = 'black', fill = '#F79420') +\n",
    "   scale_x_continuous(breaks=1:6)+\n",
    "    ggtitle('Histogram of Number times people did trips in a month')+\n",
    "    xlab('Months of the year') +\n",
    "    ylab('Number of times')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "**Summary of your question 1 results goes here.**\n",
    "\n",
    "The above histogram shows 6 months in which people did trips in. June appears to be the most common month with 37,151."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### What is the most common user type?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<ol class=list-inline>\n",
       "\t<li>'X'</li>\n",
       "\t<li>'Start.Time'</li>\n",
       "\t<li>'End.Time'</li>\n",
       "\t<li>'Trip.Duration'</li>\n",
       "\t<li>'Start.Station'</li>\n",
       "\t<li>'End.Station'</li>\n",
       "\t<li>'User.Type'</li>\n",
       "</ol>\n"
      ],
      "text/latex": [
       "\\begin{enumerate*}\n",
       "\\item 'X'\n",
       "\\item 'Start.Time'\n",
       "\\item 'End.Time'\n",
       "\\item 'Trip.Duration'\n",
       "\\item 'Start.Station'\n",
       "\\item 'End.Station'\n",
       "\\item 'User.Type'\n",
       "\\end{enumerate*}\n"
      ],
      "text/markdown": [
       "1. 'X'\n",
       "2. 'Start.Time'\n",
       "3. 'End.Time'\n",
       "4. 'Trip.Duration'\n",
       "5. 'Start.Station'\n",
       "6. 'End.Station'\n",
       "7. 'User.Type'\n",
       "\n",
       "\n"
      ],
      "text/plain": [
       "[1] \"X\"             \"Start.Time\"    \"End.Time\"      \"Trip.Duration\"\n",
       "[5] \"Start.Station\" \"End.Station\"   \"User.Type\"    "
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/html": [
       "<ol class=list-inline>\n",
       "\t<li>'X'</li>\n",
       "\t<li>'Start.Time'</li>\n",
       "\t<li>'End.Time'</li>\n",
       "\t<li>'Trip.Duration'</li>\n",
       "\t<li>'Start.Station'</li>\n",
       "\t<li>'End.Station'</li>\n",
       "\t<li>'User.Type'</li>\n",
       "\t<li>'Gender'</li>\n",
       "\t<li>'Birth.Year'</li>\n",
       "</ol>\n"
      ],
      "text/latex": [
       "\\begin{enumerate*}\n",
       "\\item 'X'\n",
       "\\item 'Start.Time'\n",
       "\\item 'End.Time'\n",
       "\\item 'Trip.Duration'\n",
       "\\item 'Start.Station'\n",
       "\\item 'End.Station'\n",
       "\\item 'User.Type'\n",
       "\\item 'Gender'\n",
       "\\item 'Birth.Year'\n",
       "\\end{enumerate*}\n"
      ],
      "text/markdown": [
       "1. 'X'\n",
       "2. 'Start.Time'\n",
       "3. 'End.Time'\n",
       "4. 'Trip.Duration'\n",
       "5. 'Start.Station'\n",
       "6. 'End.Station'\n",
       "7. 'User.Type'\n",
       "8. 'Gender'\n",
       "9. 'Birth.Year'\n",
       "\n",
       "\n"
      ],
      "text/plain": [
       "[1] \"X\"             \"Start.Time\"    \"End.Time\"      \"Trip.Duration\"\n",
       "[5] \"Start.Station\" \"End.Station\"   \"User.Type\"     \"Gender\"       \n",
       "[9] \"Birth.Year\"   "
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/html": [
       "<ol class=list-inline>\n",
       "\t<li>'X'</li>\n",
       "\t<li>'Start.Time'</li>\n",
       "\t<li>'End.Time'</li>\n",
       "\t<li>'Trip.Duration'</li>\n",
       "\t<li>'Start.Station'</li>\n",
       "\t<li>'End.Station'</li>\n",
       "\t<li>'User.Type'</li>\n",
       "\t<li>'Gender'</li>\n",
       "\t<li>'Birth.Year'</li>\n",
       "</ol>\n"
      ],
      "text/latex": [
       "\\begin{enumerate*}\n",
       "\\item 'X'\n",
       "\\item 'Start.Time'\n",
       "\\item 'End.Time'\n",
       "\\item 'Trip.Duration'\n",
       "\\item 'Start.Station'\n",
       "\\item 'End.Station'\n",
       "\\item 'User.Type'\n",
       "\\item 'Gender'\n",
       "\\item 'Birth.Year'\n",
       "\\end{enumerate*}\n"
      ],
      "text/markdown": [
       "1. 'X'\n",
       "2. 'Start.Time'\n",
       "3. 'End.Time'\n",
       "4. 'Trip.Duration'\n",
       "5. 'Start.Station'\n",
       "6. 'End.Station'\n",
       "7. 'User.Type'\n",
       "8. 'Gender'\n",
       "9. 'Birth.Year'\n",
       "\n",
       "\n"
      ],
      "text/plain": [
       "[1] \"X\"             \"Start.Time\"    \"End.Time\"      \"Trip.Duration\"\n",
       "[5] \"Start.Station\" \"End.Station\"   \"User.Type\"     \"Gender\"       \n",
       "[9] \"Birth.Year\"   "
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/plain": [
       "\n",
       "             Customer Subscriber \n",
       "       121      30754     121576 "
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/plain": [
       "\n",
       "              Female   Male \n",
       "  7158  89051  13882  42360 "
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "# Your solution code goes here\n",
    "# First let's join the 3 documents (add gender and year column to WDC)\n",
    "ny = read.csv('new_york_city.csv')\n",
    "wash = read.csv('washington.csv')\n",
    "chi = read.csv('chicago.csv')\n",
    "\n",
    "names(wash)\n",
    "names(ny)\n",
    "names(chi)\n",
    "wash$Gender <- \" \"\n",
    "wash$Birth.Year <- \" \"\n",
    "\n",
    "dt <- rbind(wash, ny, chi)\n",
    "table(dt$User.Type)\n",
    "table(dt$Gender)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "dt$Gender: \n",
       "             Customer Subscriber \n",
       "         4       6489        665 \n",
       "------------------------------------------------------------ \n",
       "dt$Gender:  \n",
       "             Customer Subscriber \n",
       "         1      23450      65600 \n",
       "------------------------------------------------------------ \n",
       "dt$Gender: Female\n",
       "             Customer Subscriber \n",
       "        31        324      13527 \n",
       "------------------------------------------------------------ \n",
       "dt$Gender: Male\n",
       "             Customer Subscriber \n",
       "        85        491      41784 "
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "###quick summary\n",
    "by(dt$User.Type, dt$Gender, summary) ##Subscribers are way more than customers\n",
    "library(ggplot2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAA0gAAANICAIAAAByhViMAAAACXBIWXMAABJ0AAASdAHeZh94\nAAAgAElEQVR4nOzde3zU9Z3o/+9kcmPIEILhjseGiwhUsVotUFddtd2qrGjb9bJtUY8rZL0f\nH5Vf0VpatNatWPHeg65YdNHaLovUrni01ksr7bIuArVeEJTFKMWIZBICJJnM+WPanPxQwgRI\nhnx4Pv/KfL7jzPsbh/Di+/3OJJbJZCIAAHq+gnwPAADAviHsAAACIewAAAIh7AAAAiHsAAAC\nIewAAAIh7AAAAiHseoabb745FovNmTMn34PsxiuvvHLssccWFxeXlZWtX78+3+MAwIFF2P0/\nr7zySuz/Lx6PV1RUHHvssbNmzdq8eXO+B+xCDz300JIlS/b+cb7xjW8sX778uOOOmzZtWiKR\n2PsH7Ab7at8BIO8K8z3AfqesrOz000/Pft3c3Lxx48bly5cvX758wYIFy5cvr6yszO94XWTG\njBmnn376GWecsTcPsmPHjj/84Q99+vT5P//n/xQW9piX1j7ZdwDYH/SYv327zcCBAx999NH2\nK++///5JJ530+uuvz5s379prr83XYF1n3bp1Gzdu3PvH2bZtWxRFFRUVPajq9tW+A8D+wKnY\n3Rs8ePDXvva1KIreeeed9uupVGrmzJljxozp1atXSUnJqFGjrrnmmlQq1XaH6667LhaLLVmy\n5J577hk6dGjfvn07eJbW1tZ77rnnmGOOKSsrSyaTJ5988gsvvLDTfeLx+B//+MfJkydXVFT0\n6tXryCOP/OlPf7qXI331q18dMWJEFEX//M//HIvFjjvuuF1N2NzcfPvttx9zzDHJZLK0tHTk\nyJGXXXbZe++9l9165plnVlRURFG0fv367Inst9566+MPctlll8VisQcffLD94u9+97tYLDZ5\n8uS2lZ///OcnnXRSv379iouLhwwZcuqppz755JPt/5NMJnP//fdPnDgxmUz26tVrzJgx119/\n/datWzvY048P8/F9P+6442Kx2C9/+cud7vncc8+1fXOuvvrqWCy2aNGiX//61yeccEJ5eXky\nmTz++ON/9atfdWrCXHYTADqlxxxZya///u//jqJo3LhxbSvNzc2TJ09+8cUXjz766Msuu6y5\nuXnp0qVz5sx5/vnnly1bFo/HoygqLi6Oouj555//8Y9/PGXKlLKysg6e4pxzzvn5z38+duzY\n888/v66u7vHHHz/hhBMWLFjwjW98o+0+NTU1n//854899tiLLrpozZo1S5YsOe+88yorK08+\n+eQ9HmnKlCnJZPLBBx+cMGHCOeecM3To0E8cr7W1dcqUKU8++eRhhx120UUX9enT5z//8z/v\nvvvuRYsWLVu27JBDDrnooos+97nPXXvttRUVFd/5zneiKOrfv/+efbfvu+++adOm9e/f/+yz\nzx4wYEBNTc3ixYtPP/30n/zkJ23fjalTpz788MODBw+ePn16SUnJs88+e+ONNz7xxBMvvPBC\nMpnM8Zt/4YUX7rTvqVTqt7/97fz589tOx2c99thjURRlnz37yL/+9a//+Z//+Qtf+MLFF1/8\n1ltvLVmy5G/+5m+eeeaZE088MccJc9lNAOicDH+xYsWKKIpGjBjRtpJOp999992bbropHo+P\nHTu2oaGhbdO//uu/RlE0YcKElpaW7MqOHTsOO+ywKIqWLFmSXbnpppuiKCovL3/qqac6fupH\nHnkkiqJTTz217dFef/31RCLRu3fv+vr6TCbzgx/8IIqi4uLihx56qO2/mjFjRhRFU6dO3cuR\nfvazn0VRdNFFF3Uw4bx586Iomjhx4vbt29sWv/3tb0dRdPbZZ2dvfvTRR1EUHXLIIR08zqWX\nXhpF0fz589svLlu2LIqi008/PXvz8MMPj6LorbfearvDhg0bksnkhAkTsjezxymPPvroVCqV\nXWltbb3sssuiKPrWt77VwZ5+3E77nkqlEolEcXFxbW1t231aWloGDBhQUlLy0UcfZTKZ6667\nLoqigoKCX/ziF233ueWWW7Lf/Nwn3O1uAkBnORW7s7Vr17Z/V+ywYcO+853vXHXVVcuWLevd\nu3fb3Y466qhFixbdeeed2SNhURQVFxdPmTIliqJVq1ZlV2KxWBRFY8aM+eIXv9jxk86fPz+K\nomuvvbbt0UaPHv3973+/urp606ZNbXebMGHC17/+9babZ511VhRFbZ8qsm9H2slPfvKTKIqu\nv/76kpKStsVrrrmmuLh48eLF2avr9pUtW7bEYrH23+1hw4bV1tZm+y+Kovvuuy+Koh/84AfZ\nQ19RFMVisRtuuKGoqCg7Z7Sne5pMJr/yla80NTUtXLiwbfHXv/71pk2b/vZv/7b9+dyJEye2\nP3d8+eWXJxKJ3//+99l3T+cy4W53EwA6S9jtLJlMnv8XU6dOPe200wYNGnTbbbedd955bdeT\nRVH0qU996qyzzvrsZz8bRVF9ff3GjRs3btyY/YCPnSpn4sSJu33S3/72t1EUHX300e0Xr7rq\nqjlz5gwfPrxtZcKECe3v0K9fvyiK6urqumKk9jKZzMsvvxxF0aRJk9qv9+nTZ/To0U1NTa++\n+mqnHrBjf/u3f5vJZP76r//6gQceaHtnQ/YEaNbvfve7jw/Tt2/fT3/60++//372vHlWZ/c0\niqILL7wwiqL2VwG2Pw/b5vOf/3z7myUlJSNHjsxkMu+++26OE+52NwGgs1xjt7MBAwbsdGl/\nOp2+6667rrrqqi984QuvvPJKUVFRdn3x4sVz5sx5+eWXt2/f3sEDtr/ULJ1OZ6+Ha/Od73zn\nc5/73NatW0tLS3v16tXxbDtdtVZQUBBFUSaTaVvZg5Fy0dDQsH379uLi4vLy8k98qNra2k49\nYMfmzp2bTqcfeOCBiy66KIqisWPHTp48ubq6uqqqKoqibdu2NTQ0RFG0q2sWa2pq/sf/+B/t\nx+uUE088saqq6r/+679Wr159+OGHt7S0LFq0qLKy8tRTT21/t4EDB+70H2bfO/KnP/0pxwk7\n3k0A2APCbvfi8fiVV1755JNPPvXUU0888UT2BOi8efOmT5+eTCarq6uPPfbY8vLygoKCxYsX\n/+///b93+s/bQjCKokwm8/zzz7ffumnTpmyfNTc3ZzKZ7AnEPbNnI+UiO1X7gmzT2tradod9\npaio6Mc//vGsWbOWLFny5JNPPvvssz/84Q/nzp370EMPnX322dnnisVi2bdofNygQYPaP1Rn\nnz0Wi02dOvV73/vegw8+eOuttz7zzDMffvjh5ZdfvtNDZf+vtZf9/sTj8Rwn7Hg3Ozs2AETC\nLnfZU6Kvv/569ubs2bOjKHriiSeOP/74tvvs9uqowsLCT8yjZDJZX1//4Ycf7s0HIO/ZSLko\nKytLJBKNjY1btmzZ6XNDPvjgg6gzB8Y+sRHff//9j98z+37S6dOnb9++/cEHH7z88sunT58+\nZcqU0tLS8vLyurq6Sy+9dI/feNuxCy64YPbs2T/96U/nzJmTvdhu6tSpO93nww8/3Glly5Yt\nURQNHDiwUxPuajfbX8sIADlyjV2u3nzzzegvp9t27NhRU1NTVlbWPqEymczSpUv37MGzF8Y9\n88wz7Rd/8IMfnHLKKS+99FIuj7DPR/rECbPXArbZvHnzG2+80atXr/YfBNOx0tLSKIqy759t\ns3z58vY3169f3z71SktLq6urJ02atGXLlnXr1kVR9LnPfS6Koo9/zt+++rVvn/rUp0488cSa\nmpqlS5f+27/925gxY7K7395//Md/tL9ZX1//+uuvx+Pxgw8+OMcJd7ubANBZwm73Wltb77zz\nzl/96lclJSXZN0KWlJT069evoaFhw4YN2ftkMpnZs2dnL4rPHrnplPPPPz+Kojlz5rR9gO07\n77xzyy23LFu2bMyYMbk8wt6MlI2tjx+Cai97HdhNN93U1NTUtnjTTTe1tLR87Wtfy/3wUvbA\nZ/bjV7Irr732WvY9pFkrV6781Kc+9fWvf739E9XX169bty4ejw8YMKBtmO9+97vZ44VZL774\n4sCBA//u7/4ux0mydrXvF1xwQRRFl156aUNDwyd+qtyvfvWr7Dsksh588MGmpqbjjz++T58+\nuUyYy24CQGc5FbuzjRs3fvWrX227mUqlXnvttXfffTcej//4xz8eNmxYdv2CCy740Y9+dPLJ\nJ2eb7Iknnvjoo49+8pOf/M3f/M2jjz568MEHZ39ZRY6+8Y1v/PznP3/iiSfGjRt36qmnbt26\ndfHixfX19ffdd1/2GGEu9nikMWPGZH/dwkUXXVRcXHzvvfd+4oSLFi16/PHHjz766FNPPbWo\nqOj3v//9r371q0MPPfTmm2/OfU+/8pWvfOtb33r++ec///nPT5gw4f3333/iiSdmzZp1zTXX\nZC/XGz9+/N///d8vXLhwzJgxp5566kEHHVRbW/vLX/7y3XffvfLKKw866KAois4+++zFixc/\n8sgjn/nMZ84555xkMvmHP/xhyZIlvXr1uuaaa3IfpoN9/+pXv3rZZZe9/fbbBQUF7T9ips3X\nv/71L37xi1/+8pdHjhy5Zs2af/mXfykqKsp+eF4uE+aymwDQad3/0Xn7rewHFO+kvLz88MMP\nv+iii1auXNn+ztu2bbvuuutGjBhRUlJy8MEHX3LJJdmPtL3gggt69+49aNCgVatWZT9V+JZb\nbsnl2Zubm2+99dYjjjiiV69evXv3Pv7445999tm2rZ/4UGvWrImiaPz48Xs/0s0331xZWVlS\nUnLUUUd1MOHcuXOPOuqoRCJRUlJy2GGHzZw5M/uZvVm5fEBxJpNZvXr1SSedlEgkysrKPve5\nzy1evDh7WOvEE0/M3iGdTt99992TJk2qrKyMx+Pl5eV/9Vd/9cADD7S2trY9SDqdvu+++7K/\nsKuwsHDYsGFTp0597bXXOv6OfaJd7Xv2qNtJJ5200/2zH1B8zz33PPPMMyeccEJZWVlZWdkJ\nJ5zwwgsvtL/bbifMZTcBoFNimU+6lh/4wQ9+cO211z700EM7HbH79re//f3vf//OO+/M/iYJ\nANh/uMYOPkFzc/O9995bWVnZ2Yv2ACCPhB18ghkzZmzYsOGKK67wsSMA9CDePAH/z+uvv/7g\ngw/+9re//c1vfjN+/PhvfvOb+Z4IADrBETv4f957771bbrnllVdeOe+8855++und/pI3ANiv\nePMEAEAgHLEDAAiEsAMACISwAwAIhLADAAiEsAMACISwAwAIhLADAAiEsAMACIRfKfZndXV1\n+R6BXSopKSksLGxsbPR52vQgRUVFxcXF27dvT6fT+Z4FclVYWFhSUtLU1NTc3JzvWdil8vLy\nXW0Sdn/mFbw/Ky0tLSwsbGlpaW1tzfcskKuioqLCwsLW1lY/XuhBCgoKCgsLd+zY4XXbQzkV\nCwAQCGEHABAIYQcAEAhhBwAQCGEHABAIYQcAEAhhBwAQCGEHABCIbvqA4pqamttuu+2tt95a\nvHhx2+LmzZsfeOCBlStXNjU1DR8+/MILLzz00EOjKLriiiveeeedtruVlpY+9thjURQ1NDTM\nmzdv1apVzc3No0ePrq6uHjBgwB6sAwAEKdYNv6PpxRdfvP/++z/zmc8899xz7cPu6quvLi4u\nnjZtWq9evRYuXLhixYr777+/tLT0f/7P//nlL395woQJ2bsVFBT069cviqIbb7yxoaFh+vTp\nJSUlCxcufOedd+64446CgoLOrn/ikLW1tV39fWCPJZPJkpKSzZs3+80T9CCJRCKRSKRSqaam\npnzPArkqKSlJJpNbt27dtm1bvmdhlyorK3e1qTtOxTY3N8+ZM6ct1LLq6+v79+9/6aWXDh8+\nfPDgwVOnTk2lUhs2bMhuGjRoUOVfZKuutrZ2+fLl06ZNq6qqGjJkSHV1dU1NzerVqzu73g37\nCwCQF91xKvakk06Komjt2rXtF5PJ5MyZM9tufvjhhwUFBZWVlc3NzTt27Fi2bNnDDz9cX18/\ncuTIqVOnDh06dM2aNUVFRVVVVdn7l5WVDRs27I033mhsbOzU+vjx47thlwEAul83XWPXsfr6\n+jvvvPPMM8+sqKioq6vr27dvS0vLJZdcEkXRI488MnPmzHvvvTeVSiWTyVgs1vZflZeX19XV\nlZeXd2q97eY999yzbNmy7NfJZPKOO+7o8v1kT8Xj8SiK+vTpk+9BoBOyF3707t07kUjkexbI\nVfbvzV69epWUlOR7Fj5Zx1cl5T/s3n333RtuuOHII488//zzoygqLy9fsGBB29YZM2acf/75\nL730UvSXV9vHdXY967333nvttdeyX1dUVBQW5v9bQcf8P6Inyv6zBHqWgoKCXV2STt6l0+kO\ntub5b8qVK1f+8Ic/PO+88yZPnvyJd+jVq1f//v1ra2uHDx+eSqUymUxbrtXV1VVUVPTt27dT\n622PfOONN954441tN715Yn/mzRP0RN48QU/kzRM9Qp7fPLErf/zjH//pn/7p6quvbl9169ev\nv+uuu1paWrI3t2/f/sEHHwwaNGjUqFHNzc1tF+pl32kxZsyYzq534/4BAHSr7jhi99FHH6XT\n6fr6+ugvB8bKysoKCgrmzp17xhlnHHLIIW1Hy8rKyvr167ds2bKWlpZzzz03nU4vWLCgrKxs\n0qRJJSUlEydOvPvuu6+44ori4uL7779/xIgRY8eOjcVinVrvhv0FAMiL7vgcu3/4h3/YtGnT\nTiuHHHLI9ddfv9M9p0+ffvrpp69bt27+/PnZt8GOHj364osvHjhwYBRFjY2N8+bNW7FiRTqd\nHjduXHV1dfbUamfXP5FTsfszp2LpiZyKpSdyKrZH6OBUbHeEXY8g7PZnwo6eSNjREwm7HmE/\nvcYOAIB9SNgBAARC2AEABELYAQAEQtgBAARC2AEABELYAQAEQtgBAARC2AEABELYAQAEQtgB\nAARC2AEABKIw3wMAwL732GOPPfXUU/meoueJx+OFhYUtLS3pdDrfs/Q8n/3sZ//xH/8xvzPE\nMplMfifYT9TW1uZ7BHYpmUyWlJRs3ry5tbU137NArhKJRCKRSKVSTU1N+Z7lQHTKKaesXLky\n31NwYOnXr98bb7zRDU9UWVm5q02O2AEQoEwmUxSPrbx+aL4H4UBx2p0b61rzf7BM2AEQplgU\nVVX6a45uUhSPRfvBWSVvngAACISwAwAIhLADAAiEsAMACISwAwAIhLADAAiEsAMACISwAwAI\nhLADAAiEsAMACISwAwAIhLADAAiEsAMACISwAwAIhLADAAiEsAMACISwAwAIhLADAAiEsAMA\nCISwAwAIhLADAAiEsAMACISwAwAIhLADAAiEsAMACISwAwAIhLADAAiEsAMACISwAwAIhLAD\nAAiEsAMACISwAwAIhLADAAiEsAMACISwAwAIhLADAAiEsAMACISwAwAIhLADAAiEsAMACISw\nAwAIhLADAAiEsAMACISwAwAIhLADAAiEsAMACISwAwAIRGG+B9hf9O7dO98jsEuFhYVRFCUS\niUwmk+9ZIFfZ121paWlRUVG+ZzkQFRQ4ckEedENOtLa2drBV2P1ZS0tLvkdgl7J/L7a0tAg7\nepBsWKTTaT9e8sKPC/KiG/68d/zaFnZ/tmPHjnyPwC4VFxcXFhY2NTV1/M8U2K/E4/Eoipqb\nm5uamvI9y4FI2JEXec8JR6oBAAIh7AAAAiHsAAACIewAAAIh7AAAAiHsAAACIewAAAIh7AAA\nAiHsAAACIewAAAIh7AAAAiHsAAACIewAAAIh7AAAAiHsAAACIewAAAIh7AAAAiHsAAACIewA\nAAIh7AAAAiHsAAACIewAAAIh7AAAAiHsAAACIewAAAIh7AAAAiHsAAACIewAAAIh7AAAAiHs\nAAACIewAAAIh7AAAAiHsAAACIewAAAIh7AAAAiHsAAACIewAAAIh7AAAAiHsAAACIewAAAIh\n7AAAAiHsAAACIewAAAIh7AAAAiHsAAACIewAAAIh7AAAAiHsAAACIewAAAIh7AAAAiHsAAAC\nIewAAAIh7AAAAiHsAAACIewAAAIh7AAAAiHsAAACIewAAAIh7AAAAiHsAAACIewAAAIh7AAA\nAiHsAAACUdg9T1NTU3Pbbbe99dZbixcvbltsaGiYN2/eqlWrmpubR48eXV1dPWDAgG5YBwAI\nUnccsXvxxRevvfbaYcOG7bQ+d+7cTZs2zZo165ZbbkkkErNnz25tbe2GdQCAIHVH2DU3N8+Z\nM2fChAntF2tra5cvXz5t2rSqqqohQ4ZUV1fX1NSsXr26q9e7YX8BAPKiO07FnnTSSVEUrV27\ntv3imjVrioqKqqqqsjfLysqGDRv2xhtvNDY2dun6+PHjsyvvvfdeXV1d9ut4PO4s7f6soKAg\niqLCwkLHXOlBsq/beDxeWNhNF73QXiwWy/cIHIi64c97JpPpaICufvpdSaVSyWSy/R+88vLy\nurq68vLyLl1vu3nPPfcsXbo0+3VFRcXTTz/dFbvJPtSnT598jwCd1rt373yPcICKx+P5HoED\nTiwW69u3b1c/Szqd7mBrPv8duat/TnX1etYxxxyTSCSyXycSie3bt3dwZ/KrqKgoHo/v2LGj\n43+mwH6lsLCwsLCwqanJkea88G2n+2UymW7IidbW1raA+bi8hV3fvn1TqVQmk2nLr7q6uoqK\niq5ebxtgypQpU6ZMabtZW1vb1bvMHksmk/F4fOvWrX5S04MkEonCwsLt27c3NTXle5YDkR8X\n5EVDQ0M3PEsHYZe3z7EbNWpUc3Nz24V3qVRqw4YNY8aM6er17t1LAIDu0x1h99FHH9XW1tbX\n10dRVFtbW1tbu3379n79+k2cOPHuu+9+++23s59yN2LEiLFjx3b1ejfsLwBAXsS64aKlf/iH\nf9i0adNOK2eccUZjY+O8efNWrFiRTqfHjRtXXV2dPVXa1eufyKnY/VkymSwpKdm8ebNzK/Qg\niUQikUikUimnYvPi5JNPfv3V1XW3H5LvQThQHDG7pra57M033+yG56qsrNzVpu4Iux5B2O3P\nhB09kbDLL2FHN9tPws7vigUACISwAwAIhLADAAiEsAMACISwAwAIhLADAAiEsAMACISwAwAI\nhLADAAiEsAMACISwAwAIhLADAAiEsAMACISwAwAIhLADAAiEsAMACISwAwAIhLADAAiEsAMA\nCISwAwAIhLADAAiEsAMACISwAwAIhLADAAiEsAMACISwAwAIhLADAAiEsAMACISwAwAIhLAD\nAAiEsAMACISwAwAIhLADAAiEsAMACISwAwAIhLADAAiEsAMACISwAwAIhLADAAiEsAMACISw\nAwAIhLADAAiEsAMACISwAwAIhLADAAiEsAMACISwAwAIhLADAAiEsAMACISwAwAIhLADAAiE\nsAMACISwAwAIhLADAAiEsAMACISwAwAIhLADAAiEsAMACISwAwAIhLADAAiEsAMACISwAwAI\nhLADAAhEYb4H2F9UVFTkewR2qaCgIIqi8vLyfA8CnRCLxaIoKisry2Qy+Z7lQBSPx/M9Agec\nWCzWDTnR2trawVZh92cfffRRvkdgl5LJZElJSV1dXcevZtivJBKJRCLR0NDQ1NSU71kOROl0\nOt8jcMDJZDLdkxOVlZW72uRULABAIIQdAEAghB0AQCCEHQBAIIQdAEAghB0AQCCEHQBAIIQd\nAEAghB0AQCCEHQBAIIQdAEAghB0AQCCEHQBAIIQdAEAghB0AQCCEHQBAIIQdAEAghB0AQCCE\nHQBAIIQdAEAghB0AQCCEHQBAIIQdAEAghB0AQCCEHQBAIIQdAEAghB0AQCCEHQBAIIQdAEAg\nhB0AQCCEHQBAIIQdAEAghB0AQCCEHQBAIIQdAEAghB0AQCCEHQBAIIQdAEAghB0AQCCEHQBA\nIIQdAEAghB0AQCCEHQBAIIQdAEAghB0AQCCEHQBAIIQdAEAghB0AQCCEHQBAIIQdAEAghB0A\nQCCEHQBAIIQdAEAghB0AQCCEHQBAIIQdAEAghB0AQCCEHQBAIIQdAEAghB0AQCCEHQBAIIQd\nAEAghB0AQCAK8/XEq1evvu6663ZanD59+umnn37FFVe88847bYulpaWPPfZYFEUNDQ3z5s1b\ntWpVc3Pz6NGjq6urBwwYsAfrAABBylvYHXbYYQ888EDbzU2bNn33u9894ogjoihqaGiYNm3a\nhAkTspsKCv58WHHu3LkNDQ2zZs0qKSlZuHDh7Nmz77jjjoKCgs6ud//OAgB0g7xVTlFRUWU7\njzzyyFlnnXXwwQdHUVRfXz9o0KC2Tf369YuiqLa2dvny5dOmTauqqhoyZEh1dXVNTc3q1as7\nu56v/QUA6Gp5O2LX3osvvvj+++/PmjUriqLm5uYdO3YsW7bs4Ycfrq+vHzly5NSpU4cOHbpm\nzZqioqKqqqrsf1JWVjZs2LA33nijsbGxU+vjx4/Pyz4CAHS1/Idda2vrwoULzz333MLCwiiK\nGhsb+/bt29LScskll0RR9Mgjj8ycOfPee+9NpVLJZDIWi7X9h+Xl5XV1deXl5Z1ab7v5+OOP\nv/rqq9mvE4lEdXV1V+8peyz72ujdu3cmk8n3LJCr7Ou2tLS0uLg437MciFx4Q16UlZV19VO0\ntrZ2sDX/Yffb3/52+/btf/3Xf529WV5evmDBgratM2bMOP/881966aUoitpXWnudXc9avnz5\n0qVLs19XVFRcddVVezA83amkpCTfI0Cnqbp8EXZ0v1gsVlpa2tXPkk6nO9ia/7D79a9/PWnS\npHg8/olbe/Xq1b9//9ra2uHDh6dSqUwm05ZrdXV1FRUVffv27dR62yNfcsklX/va17Jfx+Px\nLVu2dNUestd69+5dVFSUSqU6/mcK7FdKS0tLS0u3bt3a3Nyc71kORB3/5QddIZPJdENOZDKZ\n9j2zkzyH3datW1esWDFlypS2lfXr1//iF7+orq7OnsXYvn37Bx98MGjQoFGjRjU3N69du3bk\nyJFRFKVSqQ0bNowZM2bw4MGdWm97oiFDhgwZMqTtZm1tbbftNZ2V7bmWlhZhRwYJj48AACAA\nSURBVA+Sfbmm0+mWlpZ8z3IgcuUGeZH3P+95PlL91ltvpdPpwYMHt63069dv2bJld91118aN\nG2tqam677baysrJJkyb169dv4sSJd99999tvv51dHzFixNixYzu7nsedBQDoUrH8/pvmueee\nu+222/71X/81e3wua926dfPnz8++DXb06NEXX3zxwIEDoyhqbGycN2/eihUr0un0uHHjqqur\ns4ciO7v+iRyx258lk8mSkpLNmzc7YkcPkkgkEolEKpVqamrK9ywHopNPPvn1V1fX3X5Ivgfh\nQHHE7Jra5rI333yzG56rsrJyV5vyHHb7D2G3PxN29ETCLr+EHd1sPwk7bxoCAAiEsAMACISw\nAwAIhLADAAiEsAMACISwAwAIhLADAAiEsAMACISwAwAIhLADAAiEsAMACISwAwAIhLADAAiE\nsAMACISwAwAIhLADAAiEsAMACISwAwAIhLADAAiEsAMACISwAwAIhLADAAiEsAMACISwAwAI\nhLADAAiEsAMACISwAwAIhLADAAiEsAMACISwAwAIhLADAAiEsAMACISwAwAIhLADAAiEsAMA\nCISwAwAIhLADAAiEsAMACISwAwAIhLADAAiEsAMACISwAwAIhLADAAiEsAMACISwAwAIRGGO\n92tsbKyrqxs8eHAURdu2bfvpT3/64YcfnnXWWcOHD+/K8QAAyFVOR+xef/31qqqqn/zkJ1EU\ntbS0HH/88RdeeOE3v/nNo446asWKFV08IQAAOckp7K677rqBAwf+3d/9XRRFjz766H/+53/e\nc889b7311rhx42666aYunhAAgJzkFHa/+c1vvvWtb40YMSKKokWLFn3605/+x3/8xxEjRlx6\n6aW///3vu3hCAAByklPYbdmyJXt1XTqdfu6550477bTsev/+/f/0pz914XQAAOQsp7AbOHDg\nunXroih69tlnP/rooy996UvZ9Q0bNhx00EFdOB0AADnL6V2xX/ziF7/97W+/9dZbjzzyyIgR\nI44//vgoijZt2nT77bd//vOf7+IJAQDISU5hd8MNN7z66qs333xzZWXlL37xi3g8HkXRFVdc\nsX79+oceeqiLJwQAICc5hd3gwYOXLVuWSqV69epVVFSUXfzmN795++23Dxw4sCvHAwAgVzld\nY/fZz372tdde69OnT1vVZRd/85vfjB07tstmAwCgE3IKu5dffnnr1q07Lba0tLz66qtr167t\ngqkAAOi03ZyKjcVi2S+OOeaYT7zDUUcdtY8nAgBgj+wm7F555ZXnn3/+yiuvnDJlSmVlZftN\nsVhsyJAhF198cVeOBwBArnYTduPHjx8/fvy///u/33LLLaNGjeqemQAA2AM5vSt26dKlXT0H\nAAB7Kac3T2zatOmCCy4YOnRoPB6PfUxXjwgAQC5yOmJ32WWX/du//dsJJ5zwhS98obAwp/8E\nAIBullOlPfvssz//+c+nTJnS1dMAALDHcgq7bdu2TZo0qatHya+SkpJ8j8AuZX+LXXFxcSaT\nyfcskKvs67aoqMglK3nh205edENOdPxXYU5hd/TRR7/66qsnnnjivplov+QU8/4s+wO6sLBQ\n2NGDFBQURH/JO7qfsCMvuiEnWltbOxogl4e47bbbLrnkkrlz506cOHEfTbXf+fiv1mD/UVBQ\nEI/HGxsbO341w34lkUgUFRVt3769qakp37MciPy4IC+6Jyd69+69q005hd2VV175/vvvT5o0\nKZFI9O/ff6et77zzzt4MBwDAPpFT2BUUFBx66KGHHnpoV08DAMAeyynsXnjhha6eAwCAvZTT\nBxQDALD/y+mIXWVl5a42NTU1pVKpfTcPAAB7KKewO+6443Zaef/991evXj1ixIgTTjihC6YC\nAKDTcgq7xYsXf3xx48aN55xzzqmnnrqvRwIAYE/s+TV2gwYNuvXWW2fNmrUPpwEAYI/t1Zsn\nhg0b9sc//nFfjQIAwN7Y87DLZDIPPPDAQQcdtA+nAQBgj+V0jd2RRx6500o6nd64cWNtbe03\nv/nNLpgKAIBO28NfVVtUVHTEEUdMmTKlurp63w4EAMCeySnsXnnlla6eAwCAvdSJI3Yffvjh\n7373u/fee6+goGDYsGGTJk1KJpNdNxkAAJ2SU9i1trbOmDHjjjvuaG5ublvs3bv3rFmzrrnm\nmi6bDQCATsgp7G699dZbb731rLPOmjx58uDBg1tbW2tqahYtWjRjxoyBAwdOnTq1q6cEAGC3\ncgq7+fPnX3311bfeemv7xWnTpk2fPv32228XdgAA+4OcPsdu3bp1p59++sfXp0yZ8tprr+3r\nkQAA2BM5hV1hYWFjY+PH15ubm+Px+L4eCQCAPZFT2H3mM5/50Y9+1NTU1H5x+/bt99xzz2c/\n+9muGQwAgM7J6Rq7mTNnTp48edSoUaeddtrQoUMzmcyGDRt++ctfbty48amnnurqEQEAyEVO\nYXfaaactWrRo5syZP/7xj9sWDz/88Pvuu++UU07pstkAAOiEXD+g+MwzzzzzzDPfe++9mpqa\nWCx28MEHDxw4sEsnAwCgU3Yfdhs3bozH4/3794+iaMiQIUOGDImi6He/+11RUVG/fv26fEAA\nAHKzmzdPPPHEE4cddti//Mu/7LR+wQUXHHbYYX6HLADA/qOjsFuzZs25555bVlZ2xBFH7LTp\ngQceiMfjp5122kcffdSV4wEAkKuOwu6uu+5qamp65plnTjrppJ02TZo06cknn9y0adNdd93V\nleMBAJCrjsLuqaee+spXvnLYYYd94tYjjzxy8uTJCxcu7JrBAADonI7C7t133z388MM7uMNR\nRx319ttv7+uRAADYE7t580RBQUd3aG1tLS4u3qfzAACwhzrqtqqqquXLl3dwh+eff76qqmpf\njwQAwJ7oKOxOO+20xx9//OWXX/7ErU888cRzzz13xhlndM1gAAB0Tkdhd/XVV5eXl3/pS196\n9NFH0+l02/q2bdvmzp179tln9+/f/3/9r//V9UMCALB7Hf3miYEDBz7++ONnnXXWeeedd9ll\nl40fPz6ZTG7evHnFihUNDQ2DBg1asmSJXz4BALCf2M2vFDvuuOP+8Ic/3H777Y8//vjzzz+f\nTqcLCwvHjh375S9/+fLLL1d1AAD7j93/rtiBAwfedNNNN910UyaTaWxsTCQSsVisGyYDAKBT\ndh92bWKxWO/evbtuFAAA9sZuPscOAICeQtgBAARC2AEABELYAQAEQtgBAARC2AEABELYAQAE\nQtgBAARC2AEABELYAQAEQtgBAARC2AEABELYAQAEQtgBAARC2AEABELYAQAEQtgBAARC2AEA\nBELYAQAEQtgBAARC2AEABELYAQAEQtgBAARC2AEABELYAQAEQtgBAASiMI/PfcUVV7zzzjtt\nN0tLSx977LEoihoaGubNm7dq1arm5ubRo0dXV1cPGDBgH64DAAQpn2HX0NAwbdq0CRMmZG8W\nFPz58OHcuXMbGhpmzZpVUlKycOHC2bNn33HHHQUFBftqPX97DADQhfJZOfX19YMGDar8i379\n+kVRVFtbu3z58mnTplVVVQ0ZMqS6urqmpmb16tX7aj2P+wsA0KXydsSuubl5x44dy5Yte/jh\nh+vr60eOHDl16tShQ4euWbOmqKioqqoqe7eysrJhw4a98cYbjY2N+2R9/Pjx3b+zAADdIG9h\n19jY2Ldv35aWlksuuSSKokceeWTmzJn33ntvKpVKJpOxWKztnuXl5XV1deXl5ftkve3mt7/9\n7aVLl2a/rqioePrpp7tuZ9knssd0oWfp06dPvkc4QBUW5vNaIw5MsVissrKyq58lnU53sDVv\nr/vy8vIFCxa03ZwxY8b555//0ksvRVHUvsba21frWUOGDBkzZkz262Qy2dLSksvY5EU8Ho/F\nYv4f0bMUFBQUFBSk0+lMJpPvWQ5Evu3kRTf8VdXa2hqPx3e1dX/5B02vXr369+9fW1s7fPjw\nVCqVyWTasqyurq6ioqJv3777ZL3tGS+55JLswcKs2tra7thP9kgymSwpKUmlUq2trfmeBXKV\nSCQSicTWrVubmpryPcuBqOOjGtAVMpnMli1buuGJOjgumLc3T6xfv/6uu+5qC9vt27d/8MEH\ngwYNGjVqVHNz89q1a7PrqVRqw4YNY8aM2Vfr3buXAADdJ29h169fv2XLlt11110bN26sqam5\n7bbbysrKJk2a1K9fv4kTJ959991vv/12dn3EiBFjx47dV+v52l8AgK4Wy+NVCOvWrZs/f372\nbbCjR4+++OKLBw4cGEVRY2PjvHnzVqxYkU6nx40bV11dnT2Fuq/WP5FTsfuz7KnYzZs3OxVL\nD5I9FZtKpZyKzYuTTz759VdX191+SL4H4UBxxOya2uayN998sxueq4NTsfkMu/2KsNufCTt6\nImGXX8KObrafhJ1fwwAAEAhhBwAQCGEHABAIYQcAEAhhBwAQCGEHABAIYQcAEAhhBwAQCGEH\nABAIYQcAEAhhBwAQCGEHABAIYQcAEAhhBwAQCGEHABAIYQcAEAhhBwAQCGEHABAIYQcAEAhh\nBwAQCGEHABAIYQcAEAhhBwAQCGEHABAIYQcAEAhhBwAQCGEHABAIYQcAEAhhBwAQCGEHABAI\nYQcAEAhhBwAQCGEHABAIYQcAEAhhBwAQCGEHABAIYQcAEAhhBwAQCGEHABAIYQcAEAhhBwAQ\nCGEHABAIYQcAEAhhBwAQCGEHABAIYQcAEAhhBwAQCGEHABAIYQcAEAhhBwAQCGEHABAIYQcA\nEAhhBwAQCGEHABAIYQcAEAhhBwAQCGEHABAIYQcAEAhhBwAQCGEHABAIYQcAEAhhBwAQCGEH\nABCIwnwPsL8oLy/P9wjsUjwej6KoT58+mUwm37NArgoKCqIoSiQSvXr1yvcsB6Lszw3oTrFY\nrBtyorW1tYOtwu7Ptm7dmu8R2KXevXsXFBQ0NjZ2/GqG/UppaWk8Ht+xY0dzc3O+ZzkQ+XFB\n98tkMt2QE5lMpqSkZFdbhd2ftbS05HsEdin7A7qlpcVPanqQ7Ms1nU778ZIXDvCTF3n/8+4a\nOwCAQAg7AIBACDsAgEAIOwCAQAg7AIBACDsAgEAIOwCAQAg7AIBACDsAgEAIOwCAQAg7AIBA\nCDsAgEAIOwCAQAg7AIBACDsAgEAIOwCAQAg7AIBACDsAgEAIOwCAQAg7AIBACDsAgEAIOwCA\nQAg7AIBACDsAgEAIOwCAQAg7AIBACDsAgEAIOwCAQAg7AIBACDsAgEAIOwCAQAg7AIBACDsA\ngEAIOwCAQBTmewBgf7d06dI333wz31P0PMXFxUVFRTt27Ghpacn3LD3P8ccff+SRR+Z7Cuh5\nhB2wG9OnT29sbMz3FBxY/uqv/mrRokX5ngJ6HmEH7EZLS8vI/kW3n9sv34NwQGhJR1Pu+ZPD\nnLBnhB2we2WlsZNG98r3FBwQmtKZfI8APZg3TwAABELYAQAEQtgBAARC2AEABELYAQAEQtgB\nAARC2AEABELYAQAEQtgBAARC2AEABELYAQAEQtgBAARC2AEABELYAQAEQtgBAARC2AEABELY\nAQAEQtgBAARC2AEABELYAQAEQtgBAARC2AEABELYAQAEQtgBAARC2AEABKIwj8+9efPmBx54\nYOXKlU1NTcOHD7/wwgsPPfTQKIquuOKKd955p+1upaWljz32WBRFDQ0N8+bNW7VqVXNz8+jR\no6urqwcMGLAH6wAAQcpn2N14443FxcXf+973evXqtXDhwtmzZ99///2lpaUNDQ3Tpk2bMGFC\n9m4FBX8+rDh37tyGhoZZs2aVlJRk73/HHXcUFBR0dj1/ewwA0IXyVjn19fX9+/e/9NJLhw8f\nPnjw4KlTp6ZSqQ0bNmQ3DRo0qPIv+vXrF0VRbW3t8uXLp02bVlVVNWTIkOrq6pqamtWrV3d2\nPV/7CwDQ1fJ2xC6ZTM6cObPt5ocfflhQUFBZWdnc3Lxjx45ly5Y9/PDD9fX1I0eOnDp16tCh\nQ9esWVNUVFRVVZW9f1lZ2bBhw954443GxsZOrY8fPz678oc//GHjxo3Zr4uLiz/zmc90057T\nefF4PIqi4uLiTCaT71mA7lBQUFBSUrI3jxCLxfbVMJC7vXzd5qLjvwrzeSq2TX19/Z133nnm\nmWdWVFTU1dX17du3paXlkksuiaLokUcemTlz5r333ptKpZLJZPs/qOXl5XV1deXl5Z1ab7v5\n6KOPLl26NPt1RUXF008/3eX7yd4pKyvL9whAN4nH48lkci8fYV8NAzmKxWJ7+brNRTqd7mBr\n/sPu3XffveGGG4488sjzzz8/iqLy8vIFCxa0bZ0xY8b555//0ksvRbv+51dn17OmTJly1FFH\nZb8uKSlpaGjYs/npBqWlpYWFhVu3bnXEDg4Q6XR6L38st7a27qthIEeZTKYbciKTyXSQj3kO\nu5UrV/7whz8877zzJk+e/Il36NWrV//+/Wtra4cPH55KpTKZTFuu1dXVVVRU9O3bt1PrbY98\nzDHHHHPMMW03a2tru2QP2ReKiooKCwt37NjhJzUcIFpbW7dv376Xj7CvhoHc7eXrNkcdhF0+\n3yL6xz/+8Z/+6Z+uvvrq9lW3fv36u+66q6WlJXtz+/btH3zwwaBBg0aNGtXc3Lx27drsevad\nFmPGjOnsejfuHwBAt8rbEbumpqa5c+eeccYZhxxySNvRsrKysn79+i1btqylpeXcc89Np9ML\nFiwoKyubNGlSSUnJxIkT77777iuuuKK4uPj+++8fMWLE2LFjY7FYp9bztb8AAF0tlq+Lllau\nXHn99dfvtDh9+vTTTz993bp18+fPz74NdvTo0RdffPHAgQOjKGpsbJw3b96KFSvS6fS4ceOq\nq6uzp1Y7u/6JnIrdnyWTyZKSks2bNzu3khdDhw4dOzBa9v8NyfcgHBCa0pnyK9dPnDhxyZIl\ne/M4J5988uuvrq67/ZB9NRh07IjZNbXNZW+++WY3PFdlZeWuNuXtiN348eN39Yd2+PDhN9xw\nw8fXE4nEVVddtffrAABB8msYAAACIewAAAIh7AAAAiHsAAACIewAAAIh7AAAAiHsAAACIewA\nAAIh7AAAAiHsAAACIewAAAIh7AAAAiHsAAACIewAAAIh7AAAAiHsAAACIewAAAIh7AAAAiHs\nAAACIewAAAIh7AAAAiHsAAACIewAAAIh7AAAAiHsAAACIewAAAIh7AAAAiHsAAACIewAAAIh\n7AAAAiHsAAACIewAAAIh7AAAAiHsAAACIewAAAIh7AAAAiHsAAACIewAAAIh7AAAAiHsAAAC\nIewAAAIh7AAAAiHsAAACIewAAAIh7AAAAiHsAAACIewAAAIh7AAAAiHsAAACIewAAAIh7AAA\nAiHsAAACIewAAAIh7AAAAiHsAAACIewAAAIh7AAAAiHsAAACIewAAAIh7AAAAiHsAAACIewA\nAAJRmO8B9hfxeDzfI7BLsVgsiqJ4PJ79AgheLBbbyx/LflyQF92QE5lMpoOtwu7Pkslkvkdg\nl7J/Tnr37p3vQYBuEo/H9/LHckGBU1J0t1gs1g050dra2sFWYfdnW7ZsyfcI7FIymSwpKUml\nUh2/moFgtLS07OWP5XQ6va+GgRxlMpnuyYnKyspdbfIPGgCAQAg7AIBACDsAgEAIOwCAQAg7\nAIBACDsAgEAIOwCAQAg7AIBACDsAgEAIOwCAQAg7AIBACDsAgEAIOwCAQAg7AIBACDsAgEAI\nOwCAQAg7AIBACDsAgEAIOwCAQAg7AIBACDsAgEAIOwCAQAg7AIBACDsAgEAIOwCAQAg7AIBA\nCDsAgEAIOwCAQAg7AIBACDsAgEAIOwCAQAg7AIBACDsAgEAIOwCAQAg7AIBACDsAgEAIOwCA\nQAg7AIBACDsAgEAIOwCAQAg7AIBACDsAgEAIOwCAQAg7AIBACDsAgEAIOwCAQAg7AIBACDsA\ngEAIOwCAQAg7AIBACDsAgEAIOwCAQAg7AIBACDsAgEAIOwCAQAg7AIBACDsAgEAIOwCAQAg7\nAIBACDsAgEAIOwCAQAg7AIBACDsAgEAU5nuALtTQ0DBv3rxVq1Y1NzePHj26urp6wIAB+R4K\nAKCrhHzEbu7cuZs2bZo1a9Ytt9ySSCRmz57d2tqa76EAALpKsGFXW1u7fPnyadOmVVVVDRky\npLq6uqamZvXq1fmeCwCgqwR7KnbNmjVFRUVVVVXZm2VlZcOGDXvjjTfGjx+fx6l++ctffvjh\nh3kcoIcqLS0tLCzcunVrJpPJ9yw9z5e+9CUXIQAcIIINu1QqlUwmY7FY20p5eXldXV3bzfnz\n5y9fvjz7dVlZ2fe///2uHum///u/L7jggq5+FtjJ+vXr58yZs5cPsvaDltPv/NM+mQc61prJ\nRFFUWFhYXl6+N48Tj8dbWjNet3Sbmi0tpWWxvXzd5qLj68qCDbsoitpX3cetXbv2P/7jP7Jf\nV1RUFBUVdfU8Bx10UP/+/T/44IOufiJo79BDD93Ll/e4ceNWrFjx7Bvb9tVIsFuf/vSn9/J1\n++lPf9rrlm529Lhx3ZAT6XS6g62xUM9t/f73v7/lllt+9rOfteXd5ZdffsIJJ3z1q1/9xPvX\n1tZ243R0TjKZLCkp2bx5s7e/0IMkEolEIpFKpZqamvI9C+SqpKQkmUxu3bp12zZNvP+qrKzc\n1aZg3zwxatSo5ubmtWvXZm+mUqkNGzaMGTMmv1MBAHSdYMOuX79+EydOvPvuu99+++2amprb\nbrttxIgRY8eOzfdcAABdJdhTsVEUNTY2zps3b8WKFel0ety4cdXV1RUVFbu6s1Ox+zOnYumJ\nnIqlJ3Iqtkfo4FRsyG+eSCQSV111Vb6nAADoJsGeigUAONAIOwCAQAg7AIBACDsAgEAIOwCA\nQAg7AIBACDsAgEAIOwCAQAg7AIBACDsAgEAIOwCAQAg7AIBACDsAgEAIOwCAQAg7AIBACDsA\ngEAIOwCAQAg7AIBACDsAgEAIOwCAQAg7AIBACDsAgEAIOwCAQAg7AIBACDsAgEAIOwCAQAg7\nAIBACDsAgEDEMplMvmeA3fje9773/PPPP/roowMGDMj3LJCrBQsWPPjggzfffPOxxx6b71kg\nVy+88MJ3v/vd6dOnn3POOfmehT3hiB09wLZt21KplH+E0LNs3749lUq1tLTkexDohJaWllQq\ntWPHjnwPwh4SdgAAgRB2AACBKMz3ALB7hx9+eBRFpaWl+R4EOmHEiBGnnHJKZWVlvgeBThgw\nYMApp5zyqU99Kt+DsIe8eQIAIBBOxQIABELYAUDI0un0GWec8V//9V/79gFXrly5zx+Zveca\nO4Cotrb2Zz/72csvv7x58+aysrJDDz30rLPOGjdu3B481KpVqxKJxMiRI/f5kBBFUWtr66JF\ni1544YWNGze2tLQMHDjw5JNP/spXvhKLxbpthoKCgu9///tVVVXd9ozkTtgBB7p33333W9/6\nVt++fS+66KJhw4Zt2bLl6aefvu6662bMmDFp0qTOPtrixYuPOeYYYUcXmT9//osvvnjZZZeN\nGDEiiqJVq1bde++9O3bs+NrXvtZtM8Risex72tLpdLc9KTkSdsCB7t577y0vL//Rj35UXFwc\nRdHBBx98+OGHV1ZWrl+/ftKkSdv/b3v3H9VU/f8B/L3NsbEYHX4Olkj8iECpc4ACFuNHEB0O\npciPOBYedhggxMGDQZzkKKUZhHQCXRqJRsARKtQOoLHEQypYHlFEjnhSQEyQgA0CIhBh2/3+\ncT/fnZ0QQj9f3dfxfPx17/vXfbHzOu7l+95tMzOxsbF5eXn0O9ng4GBKSsqBAwdsbW2bmpqO\nHTumUCh4PJ5IJEpMTNy5c2dnZ2dHR0djY2NxcfH4+PjBgwc7OzunpqYcHR0TEhLc3NwoioqI\niNiyZUtTU9Pw8DCHw8nKyjpz5kxHR8f4+HhERERUVBQhZGxs7NChQ52dndPT087OzklJSU5O\nThqNZv369enp6TU1NS+88EJGRoaeXzt47K5cuRIcHPzSSy/Rp4GBgaampvTnIBfKVfo3exQK\nxdatW3t6eqytrSUSiY+PDyFkfg4bGRmNjIyUlpZeuXKFy+WKRCKpVMpms3UTLz09PTIycteu\nXe7u7gutjATWFzxjBwDL2sTExNWrV6OiouiqTis+Pv7tt99eZOLQ0JBMJktJSampqSksLLxx\n40Z9fX1eXp6VlVVSUlJxcTEh5JNPPpmampLJZFVVVa6urjt37vzrr78YDAaTyWxsbMzNzS0t\nLTU1Nd22bZubm9vevXszMjIqKysnJiYIIXl5eYSQffv2VVVVrVmzZseOHbOzs0wmk8lk/vTT\nTzk5OZs2bXqULwz8P+Xg4PDLL7/09PRoWzw8PDw9Pf91Yl1dnUQiqays9Pf3LygoUCgU981h\nQsinn37KYrEOHDhQUFBw7dq18vLyxRNv/soECaw/KOwAYFkbHh4mhNjb2z/oxKmpKYqi+Hw+\nk8m0sbEpKiqKiYnRHdDb29vV1ZWYmPj0009zOJyNGzdqNJq2tja6NzAwkMvlMplMV1dXY2Nj\nkUhECFm9erVGoxkaGrp582ZXV1dSUhKfzzcyMoqLi1OpVBcuXKDn+vr6Ojk5GRsb/7d/PDyB\nkpOTnZ2d33///eTk5KKiopMnT9L/E/hXQUFBbm5uPB4vJiZmxYoVbW1t983h3t7e7u5uiURi\nZmYmFAozMzO9vLzoFRZKvPkrI4H1CLdiAQAe5lEhR0fHsLCwrKys5557zsPDIzAwUCgU6g4Y\nHBxkMBgrV66kT42MjKysrOjNDEKIhYWFtt3c3Jw+ZrPZhJDZ2Vl6mEQi0V2QrkEJIba2tg8a\nLRgMPp+fnZ2dmpra2dl5/fr1+vr60tLS9PT0V199dfGJ2lRks9nm5uYjIyNhYWHzc5jOW4FA\nQA92dHR0dHSkjxdKvPkrm5iYECSwnqCwA4BlTSgUMhiM3t7e559/Xrdd6OlIYgAACPVJREFU\no9EwGIz5nzTUaDT0AYPBSEtLi4mJuXTp0sWLF2tqajIzM/39/Re5FkVRKpVKO32RkfR94aNH\nj/7jBjGNrv9gOePz+SKRSCQSJSQkHDp0qKSkJCAg4B9jtLlK080lJpPJZrPvm8MsFosQQlHU\n/BRdKPHmr4wE1iPcigWAZc3ExMTDw+Po0aPT09O67VVVVbm5uYQQ+v1vbm6ObtfuOqjV6omJ\nCWtr6/Dw8I8++igsLKyhoUF3BaFQSFFUf38/fTozM6NQKJa4V0Fv/t26dUvbMjQ09JB/IRgQ\npVK5e/dupVKp2+jm5nbv3r25ubmFcpU2MDBAH6hUqtHRUUtLy/vmsK2trW7ednV1/fjjj4tH\nNX9lJLAeobADgOVu06ZNs7OzGRkZzc3N/f39nZ2de/bsqauri46OJoSwWCwbG5uOjg5CyL17\n97RvcqdPn37vvfd6enooihobG+vr66PfzDgczuDg4NTUlIODg6ur6zfffDM5OTkzM1NeXm5s\nbOzr67uUkOzs7F588cWvv/5aqVSq1Wq5XL558+Y///zzkb0G8GSwsLAYGBjYtWtXa2urQqFQ\nKpWtra0VFRUeHh5cLnehXKWdOnXq9u3bKpWqtrZWo9H4+PjcN4cdHBxcXFzKysqGh4cHBga+\n/PLLvr6+xaOavzISWI9wKxYAljuhUFhcXPz999+Xl5ePj4/z+fzVq1cXFhZqHy169913v/rq\nq/Pnz5uZmcXGxl68eFGtVoeEhCiVyvz8fHqKl5eXVColhISFhVVUVJw7d66srCw7O7u0tDQt\nLY2iKBcXl4KCAh6Pt8SosrKyDh48uHnzZoqi7O3td+zYoX0UD5Yt+puBjxw5UlZWNjo6qlar\nBQKBn59fbGwsPeC+uUo/QhodHb1///7e3l6BQJCTk8Pn8xfK4dzc3H379qWnp3O5XF9f34SE\nhIXiWWhlggTWHwb95TcAAAAA8KTDrVgAAAAAA4HCDgAAAMBAoLADAAAAMBAo7AAAAAAMBAo7\nAAAAAAOBwg4AAADAQKCwAwAAADAQKOwAAAAADAQKOwAAAAADgcIOAAxfamoqg8H4/fff53c9\n++yz7u7uj+HqC1nir8cCACwFfisWAODR2rBhg7Z27O7ulslk0dHRQUFBdIuNjY3eIgMAg4PC\nDgDg0QoKCtKWcWfOnJHJZGKxOD09Xa9BAYBhwq1YAID/GBwcTE5Otre353K5NjY20dHR169f\n1/aePXs2NDTU1NSUx+N5enqWlZVpu8RicUBAwIkTJ+zs7F555ZUHuqhYLLa0tJydndVtDAoK\nsrKympub8/LyEolEP//8s7e3N4/HMzc3l0qlExMTS4kKAJYhFHYAAP8RFRV14sSJDz/8UC6X\nFxUVdXd3BwYGTk9PE0KamppCQkJmZ2erq6vr6up8fHwSExM///xzeiKHw5mYmMjOzs7Jydm2\nbdsDXVQqlY6Ojh4/flzbMjQ01NLS8s4777DZbA6Hc/PmzQ8++GDPnj19fX0ymezw4cMJCQn0\nyMWjAoDliAIAMHQpKSmEkFu3bs3vsre3X7NmDUVR9DbY1q1btV09PT35+fkDAwMURXl4eDg7\nO09NTWl7161bx+fz7969S1FUSEgIIeSHH37410hOnz5NCCkuLta2TE5OmpiYrF27VtvyxRdf\nEELa2tooivLz8yOENDc3a3sTExMJIX19ff8aFQAsQ9ixAwAghBBjY2MLC4tvv/22qalJo9EQ\nQpycnHJycoRCoUKhaG9vf+ONN5hM5sz/Cg8Pn5ycvHr1Kj3dyMjozTfffIjrmpiYvPXWW3K5\nXKFQ0C01NTXu7u6enp706VNPPSUWi7XjAwICCCGdnZ1LiQoAlhsUdgAAhBDCZrPr6uqYTOZr\nr71mbW0dExNTXV2tUqkIIX/88QchZO/evcY6UlNTCSF37tyhp1taWrLZ7Ie7tFQqValUhw8f\npq917ty5+Ph4ba9AIGAwGNpTCwsLQsjw8PBSogKA5QafigUAw8flcgkhMzMz87v+/vtv7ReO\n+Pn5dXd3nz17Vi6XNzQ0xMXFFRcXNzc3071SqTQ5Ofkf052dnemDh67qCCFisdjFxaWioiIz\nM/PIkSNMJnPjxo0LDaZrTSaTuZSoAGC5QWEHAIbP0dGREHL58mVXV1fd9u7u7tHR0bVr12pb\nWCxWcHBwcHDwZ599VlJSkpaWVlNTQw9Qq9WP7suEExIScnJyrl27Vl1dHRoaamtrq+0aHBxU\nq9UsFos+HR4eJoQIBIJVq1Y96qgA4ImDW7EAYPiioqK4XO727dvHxsa0jdPT0xkZGYQQqVRK\nCGlra9uwYYP2QTdCyOuvv04IUSqV5ubm3t7etbW14+Pj2t7Kysrt27fT+2f/PYlEwmKx8vPz\nW1tbJRKJbtfdu3cbGxu1p3K5nMPheHt7P4aoAOCJgx07ADB8K1eu3L9/f3JysouLS3x8vJ2d\n3Z07d7777ruBgYHc3Fx/f39CyDPPPNPQ0PDbb79lZGSsWrVqdHRUJpOZmppGRkYSQgoLC0ND\nQwMDA7OysmxsbFpaWnbv3h0XF7dixf/Nv6K2trZhYWHV1dWmpqYRERG6XXZ2dlu2bLl9+7az\ns/PJkydra2vj4+PNzMweQ1QA8OTR98dyAQAek19//TU6OlogEKxYscLS0jI8PFwul+sO6Ojo\niIyMtLa2ZrPZQqEwMjLy8uXL2t6WlpbQ0FA+n89ms11cXAoLC+fm5uiukJAQe3v7pcQw/+tO\ntI4dO0YISUpK0m308/NzdXW9dOlSQEAAj8czMzNLTk6enJxcSlQAsAwxKIrSd20JAADk+PHj\n69atu3Dhgre3t7ZRLBaPjIzo/gAGAMAi8IwdAID+zc3Nffzxx76+vrpVHQDAg8JzGAAA+tTf\n39/e3l5SUtLe3n7+/Hl9hwMATzbs2AEA6NOpU6fWr19/48aN+vr6l19+Wd/hAMCTDc/YAQAA\nABgI7NgBAAAAGAgUdgAAAAAGAoUdAAAAgIFAYQcAAABgIFDYAQAAABgIFHYAAAAABgKFHQAA\nAICBQGEHAAAAYCBQ2AEAAAAYiP8BSiyD4NaOMGEAAAAASUVORK5CYII=",
      "text/plain": [
       "plot without title"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "ggplot(aes(x = User.Type), data = dt) +\n",
    "    geom_bar(color = 'black', fill = '#F79420') +\n",
    "    ggtitle('Bar-chart of user types')+\n",
    "    xlab('User Type') +\n",
    "    ylab('Counts')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "**Subscribers are way more than customers with 121,576 in total**"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### What is the most common day of the month?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<ol class=list-inline>\n",
       "\t<li>'X'</li>\n",
       "\t<li>'Start.Time'</li>\n",
       "\t<li>'End.Time'</li>\n",
       "\t<li>'Trip.Duration'</li>\n",
       "\t<li>'Start.Station'</li>\n",
       "\t<li>'End.Station'</li>\n",
       "\t<li>'User.Type'</li>\n",
       "</ol>\n"
      ],
      "text/latex": [
       "\\begin{enumerate*}\n",
       "\\item 'X'\n",
       "\\item 'Start.Time'\n",
       "\\item 'End.Time'\n",
       "\\item 'Trip.Duration'\n",
       "\\item 'Start.Station'\n",
       "\\item 'End.Station'\n",
       "\\item 'User.Type'\n",
       "\\end{enumerate*}\n"
      ],
      "text/markdown": [
       "1. 'X'\n",
       "2. 'Start.Time'\n",
       "3. 'End.Time'\n",
       "4. 'Trip.Duration'\n",
       "5. 'Start.Station'\n",
       "6. 'End.Station'\n",
       "7. 'User.Type'\n",
       "\n",
       "\n"
      ],
      "text/plain": [
       "[1] \"X\"             \"Start.Time\"    \"End.Time\"      \"Trip.Duration\"\n",
       "[5] \"Start.Station\" \"End.Station\"   \"User.Type\"    "
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/html": [
       "<ol class=list-inline>\n",
       "\t<li>'X'</li>\n",
       "\t<li>'Start.Time'</li>\n",
       "\t<li>'End.Time'</li>\n",
       "\t<li>'Trip.Duration'</li>\n",
       "\t<li>'Start.Station'</li>\n",
       "\t<li>'End.Station'</li>\n",
       "\t<li>'User.Type'</li>\n",
       "\t<li>'Gender'</li>\n",
       "\t<li>'Birth.Year'</li>\n",
       "</ol>\n"
      ],
      "text/latex": [
       "\\begin{enumerate*}\n",
       "\\item 'X'\n",
       "\\item 'Start.Time'\n",
       "\\item 'End.Time'\n",
       "\\item 'Trip.Duration'\n",
       "\\item 'Start.Station'\n",
       "\\item 'End.Station'\n",
       "\\item 'User.Type'\n",
       "\\item 'Gender'\n",
       "\\item 'Birth.Year'\n",
       "\\end{enumerate*}\n"
      ],
      "text/markdown": [
       "1. 'X'\n",
       "2. 'Start.Time'\n",
       "3. 'End.Time'\n",
       "4. 'Trip.Duration'\n",
       "5. 'Start.Station'\n",
       "6. 'End.Station'\n",
       "7. 'User.Type'\n",
       "8. 'Gender'\n",
       "9. 'Birth.Year'\n",
       "\n",
       "\n"
      ],
      "text/plain": [
       "[1] \"X\"             \"Start.Time\"    \"End.Time\"      \"Trip.Duration\"\n",
       "[5] \"Start.Station\" \"End.Station\"   \"User.Type\"     \"Gender\"       \n",
       "[9] \"Birth.Year\"   "
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/html": [
       "<ol class=list-inline>\n",
       "\t<li>'X'</li>\n",
       "\t<li>'Start.Time'</li>\n",
       "\t<li>'End.Time'</li>\n",
       "\t<li>'Trip.Duration'</li>\n",
       "\t<li>'Start.Station'</li>\n",
       "\t<li>'End.Station'</li>\n",
       "\t<li>'User.Type'</li>\n",
       "\t<li>'Gender'</li>\n",
       "\t<li>'Birth.Year'</li>\n",
       "</ol>\n"
      ],
      "text/latex": [
       "\\begin{enumerate*}\n",
       "\\item 'X'\n",
       "\\item 'Start.Time'\n",
       "\\item 'End.Time'\n",
       "\\item 'Trip.Duration'\n",
       "\\item 'Start.Station'\n",
       "\\item 'End.Station'\n",
       "\\item 'User.Type'\n",
       "\\item 'Gender'\n",
       "\\item 'Birth.Year'\n",
       "\\end{enumerate*}\n"
      ],
      "text/markdown": [
       "1. 'X'\n",
       "2. 'Start.Time'\n",
       "3. 'End.Time'\n",
       "4. 'Trip.Duration'\n",
       "5. 'Start.Station'\n",
       "6. 'End.Station'\n",
       "7. 'User.Type'\n",
       "8. 'Gender'\n",
       "9. 'Birth.Year'\n",
       "\n",
       "\n"
      ],
      "text/plain": [
       "[1] \"X\"             \"Start.Time\"    \"End.Time\"      \"Trip.Duration\"\n",
       "[5] \"Start.Station\" \"End.Station\"   \"User.Type\"     \"Gender\"       \n",
       "[9] \"Birth.Year\"   "
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "# First let's join the 3 documents (add gender and year column to WDC)\n",
    "ny = read.csv('new_york_city.csv')\n",
    "wash = read.csv('washington.csv')\n",
    "chi = read.csv('chicago.csv')\n",
    "\n",
    "names(wash)\n",
    "names(ny)\n",
    "names(chi)\n",
    "wash$Gender <- \" \"\n",
    "wash$Birth.Year <- \" \"\n",
    "\n",
    "dt <- rbind(wash, ny, chi)\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<ol class=list-inline>\n",
       "\t<li>'21'</li>\n",
       "\t<li>'11'</li>\n",
       "\t<li>'30'</li>\n",
       "\t<li>'02'</li>\n",
       "\t<li>'10'</li>\n",
       "\t<li>'14'</li>\n",
       "</ol>\n"
      ],
      "text/latex": [
       "\\begin{enumerate*}\n",
       "\\item '21'\n",
       "\\item '11'\n",
       "\\item '30'\n",
       "\\item '02'\n",
       "\\item '10'\n",
       "\\item '14'\n",
       "\\end{enumerate*}\n"
      ],
      "text/markdown": [
       "1. '21'\n",
       "2. '11'\n",
       "3. '30'\n",
       "4. '02'\n",
       "5. '10'\n",
       "6. '14'\n",
       "\n",
       "\n"
      ],
      "text/plain": [
       "[1] \"21\" \"11\" \"30\" \"02\" \"10\" \"14\""
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/plain": [
       "\n",
       "       01   02   03   04   05   06   07   08   09   10   11   12   13   14   15 \n",
       "   1 4986 5184 4971 4539 4378 4283 4353 5247 5411 4958 4667 4856 4901 4485 5023 \n",
       "  16   17   18   19   20   21   22   23   24   25   26   27   28   29   30   31 \n",
       "4724 4774 5472 5252 5520 5781 4504 5213 5502 5006 5257 5917 5597 4961 4711 2017 "
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/html": [
       "'character'"
      ],
      "text/latex": [
       "'character'"
      ],
      "text/markdown": [
       "'character'"
      ],
      "text/plain": [
       "[1] \"character\""
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/html": [
       "'numeric'"
      ],
      "text/latex": [
       "'numeric'"
      ],
      "text/markdown": [
       "'numeric'"
      ],
      "text/plain": [
       "[1] \"numeric\""
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "dt$day <- substr(dt$Start.Time, 9, 10) \n",
    "head(dt$day)\n",
    "table(dt$day) ####27th day of the month was the most common day, looking at data closely from 18th, we see strickes\n",
    "\n",
    "library(ggplot2)\n",
    "class(dt$day)\n",
    "dt$day <- as.numeric(dt$day)\n",
    "class(dt$day)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "Warning message:\n",
      "“Removed 1 rows containing non-finite values (stat_bin).”"
     ]
    },
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAA0gAAANICAIAAAByhViMAAAACXBIWXMAABJ0AAASdAHeZh94\nAAAgAElEQVR4nOzdeXxTVf7/8XOzJ02aFsoqCIjI4gi4oGwCIuogaEFEHZRtGKEzKqOIDogz\nCMOgDjsK1KIooijOiAiKKCDihorIpgLKIpZNaOnepFl/f9zv5NdH29zcbKVcXs+/mpOTez/3\n3JObd5ObGykYDAoAAACc/3TnugAAAAAkBsEOAABAIwh2AAAAGkGwAwAA0AiCHQAAgEYQ7AAA\nADSCYAcAAKARBLv/b9KkSZIkZWdnn+tCzhu7du269tprTSaT3W4/evTouS5HyZNPPilJ0vPP\nP3+uCmB2qZe8nbVr1y5Jkvr06SPfVLNTqjwkZkyAcOr4yCRqAgC1RsvBTn5CXnrppeE62O12\nSZJOnTol30xPT2/RooXD4VC/ihUrVqxduzbeQs9bw4cP3759e8+ePceOHWuz2ap3kHeBJElP\nPfVUjUvo06dP5V2gJVXmRgyzC8mWqJ2i5jjABAiHkQESS8vBLlp/+9vffvnll3vvvVf9Qx5/\n/PELNthVVFR8//33qampH3300dy5cxs0aKDQ+emnn/7xxx9rrba6oMrciGF2IdkStVPUHAeY\nAOEwMkBiEexid/jwYU2+1aSSy+USQqSnpxsMBuWeHTt29Hg8999//4Xz+3UX+Ny4oLCvAdQp\nBLv/r/qpHv/973/79u1br149k8nUtGnT/v37f/DBB/Jdd955Z+vWrYUQL730kiRJPXv2lNu9\nXu+CBQu6dOnicDgsFsull1764IMPnjhxovKKfv3112HDhjVo0MBms3Xp0mX16tVnz56VJOm6\n666TO0yZMkWSpLVr1y5evPiiiy5KS0uT24uLiydPnty+fXur1Wo2m9u0afPYY48VFxeHlvz3\nv/9dfuC2bdv69OnjcDgaNGgwatSokpKSYDA4f/78du3a2Wy2Dh06PP3008oxS3lDBg0alJ6e\nLoQ4evSo/GHrwYMHwy2qZ8+ed91115dffhnxNJoHH3xQkqRXXnmlcuNXX30lSdLAgQPj30ad\nTrdly5bevXunpqba7faePXtu2rSpcodgMPjiiy9269bN4XBYrdb27dv//e9/LysrC3UIt2sq\nq3FuVJldMW9FxAqF4ryt0YQJEyRJWr16tTw4TqfT4XD06tVr8+bNUQ2OUDH/Va6rCjWrru7o\n0aP33HNPRkaGzWbr3LnzsmXLqnSo/pSP+JAqatzXNU6SKutSOQ7R7kqhYheE5t4PP/wwePDg\nhg0bWiyWzp07v/HGG8pLjnj8qVHEw13lkZHPzVi3bl2Vhbz33nuSJN14443yzYjzIeZtVDMB\nlMehZ8+ekiS9//77VR71ySefVH6lAJInwnstF7KlS5eOHTu2QYMGd911V8OGDY8fP75mzZoB\nAwYsX758+PDho0ePdjgcr7zySteuXe++++6LLrpICBEIBDIzMz/44IN27dqNGTMmNTX122+/\nXbRo0erVq7dt29aiRQshRH5+fs+ePXNzc3v06NGvX79jx47de++9Tz75pBDCYrHIqzaZTEKI\nrVu3ZmdnZ2Zm2u12IYTX6x04cOBnn3129dVXP/jgg16vd8OGDbNnz966deu2bdv0en3ogV99\n9dWSJUtuueWWkSNHvvvuu8uXLw8EAk2bNl25cuWAAQPKy8vffPPNJ554olmzZsOHD69x2yNu\nyJgxY6677ronnngiPT39H//4hxBC4aNYt9u9cOHCjRs3Tpo06fbbb5fHKmbxbOOuXbsmTJhw\nww033H///YcOHVq7dm3//v03bdrUu3dvucOIESNee+21Jk2ajBs3zmw2f/zxxzNmzHjvvfc+\n/fRT+RygGndNFTXOjURtRcQKleetwpBu2bLlpZdeuummm+6///6DBw+uXbv2lltu2bRpU+i0\n8YirVjP/Va6rioirrq6goOD666/Pzc3t1atXr169zpw5M2XKlP79+9fYOeaH1Liv1UwSNeMQ\nw65Uvwt27tw5YsSI66677r777vvpp5/ef//9YcOGNWrUqG/fvjUuWc3xpzo1h7vKhg0btnXr\n1rfffvu2226r3P7WW28JIdQ/C2LbRjUTIOI4jB49+osvvnj55ZcHDBigsAlAEgW1a+fOnUKI\n1q1bh+uQkpIihDh58qR8829/+5sQYsmSJfLNK664Qghx8ODBUP/c3FyHw9G1a1f55n/+8x8h\nxJgxY0IdcnJyhBDdunVzu92hRvkodtddd8k3p0yZIoQYOnRoqMMXX3xhtVqFEL1795ZbZs6c\nKYRwOp0ffvhhqNvbb78thOjatavP55NbKioq2rVrJ4RYu3at3PL0008LIcxm85YtW+SWo0eP\n6vV6o9HYrl27/Px8ufHFF18UQgwcODDcyKjZkIKCAiFEixYtwi0k+L9dMGrUqNAyBw0aVLmD\n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\nCwsLDx8+XOND5BMvvvjii8qNZ8+ePXDggNVqvfzyy/V6fatWrfx+//79+yv32bBhg3IxFRUV\nx48ft9vtlY8mwWAw4gNjE3FD4ll4jx49xo4du3///pkzZ1b51EO+AoL8tYyQ7du3x7O6yuSz\np0MqKioOHDig0+nkL7XJJ9N8+umnVR519uzZRBUQJzUVxjBvZd98803lmyUlJfv379fr9c2b\nN1e5avXTRnldVcSwX/R6fZs2bYQQe/bsqdz++eefJ/Ah8VMeh2QcgmKrM7bjT8yHu5tvvjkj\nI2PdunUul2vdunXt2rWTt0uWpOepmgmgfhxatmzZp0+f48ePb9iw4Z133mnfvn3lTQCSimBX\ns927d7ds2fK+++7zeDyhxpKSksOHD+v1+oYNG4r/pZDK/3PLp8LMnDmz8qNmzpzp8/nuvfde\n+T/sW265RQjx3HPPhTp888038r90Csxmc7169UpLS0P/7AaDwenTp8tnCsv/5SeQmg2Jx7PP\nPtukSZNnnnnm+PHjldsvueQS8b+rBsgt+/btW7p0aZyrC9m8efOXX34Zurl06VKXy3XDDTfI\n31GQt/qpp56S396QffbZZ40aNRo6dGhUK6o+NxIiYoVq5m04mzdvlk9Ll73yyisej6dXr17q\nB0f9tFFeV7RbXaNbb71VCDF37txQy5EjR1566SWFEYjhISK+fa0wDrHtyiQ9c2M+/sR2uDMY\nDEOHDs3NzZ03b15ZWdl9991X+d4EPk+riDgBohqHUaNGCSEeeOCB0tJSvjaB2sRHsTXr1KnT\nsGHDVq5c2b59+/79+9evXz8vL+/9998/duzYX//6V/l02vbt28tXGB8zZozJZFqyZMnw4cNX\nr1797rvvXn311f379zcajV9//fXmzZsvu+yyZ555Rl7yxIkTX3vttRdeeOHo0aPXXnvt0aNH\nV69e/eSTT8pfmFcwatSouXPn3njjjSNHjhRCvPfeewUFBcuXL7/lllvefPPN5s2bJ/DHFtVs\nSDycTufChQuHDh26a9euyu1DhgyZNGnS1q1be/To0bVr15MnT7733ntTp0597LHH5JOEYubz\n+YQQY8aM6d+//+DBgy+55JJ9+/b95z//MZvN//rXv+Q+d91115o1a954440rr7zy7rvvdjgc\n33///dq1a61W62OPPRbV6qrPjXiKD4lYoZp5G8599913880333HHHZdeeunPP//8+uuvG41G\n+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",
      "text/plain": [
       "plot without title"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "ggplot(aes(x = day), data = dt) +\n",
    "    geom_histogram(binwidth = 1, color = 'black', fill = '#F79420') +\n",
    "   scale_x_continuous(breaks=1:31)+\n",
    "    ggtitle('Histogram of Number times people did trips on a given day')+\n",
    "    xlab('days of the month') +\n",
    "    ylab('Number of times')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "We see strikes and trough in terms common dayy. The 27th day "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "\n",
    "## Finishing Up\n",
    "\n",
    "> Congratulations!  You have reached the end of the Explore Bikeshare Data Project. You should be very proud of all you have accomplished!\n",
    "\n",
    "> **Tip**: Once you are satisfied with your work here, check over your report to make sure that it is satisfies all the areas of the [rubric](https://review.udacity.com/#!/rubrics/2508/view). \n",
    "\n",
    "\n",
    "## Directions to Submit\n",
    "\n",
    "> Before you submit your project, you need to create a .html or .pdf version of this notebook in the workspace here. To do that, run the code cell below. If it worked correctly, you should get a return code of 0, and you should see the generated .html file in the workspace directory (click on the orange Jupyter icon in the upper left).\n",
    "\n",
    "> Alternatively, you can download this report as .html via the **File** > **Download as** submenu, and then manually upload it into the workspace directory by clicking on the orange Jupyter icon in the upper left, then using the Upload button.\n",
    "\n",
    "> Once you've done this, you can submit your project by clicking on the \"Submit Project\" button in the lower right here. This will create and submit a zip file with this .ipynb doc and the .html or .pdf version you created. Congratulations!"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [],
   "source": [
    "system('python -m nbconvert Explore_bikeshare_data.ipynb')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "R",
   "language": "R",
   "name": "ir"
  },
  "language_info": {
   "codemirror_mode": "r",
   "file_extension": ".r",
   "mimetype": "text/x-r-source",
   "name": "R",
   "pygments_lexer": "r",
   "version": "3.5.1"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
