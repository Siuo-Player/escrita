# Cast Naming Draw Audit — First Supporting-Cast Pass

Status: WORKING / reproducible draw record; names are not author-locked
Updated: 2026-10-12

## Purpose

This pass creates enough recurring people to test natural pacing in the opening episodes without falling back on the model's most stereotyped names. Roles were defined from narrative function first; names were assigned from constrained, period-appropriate candidate pools afterward. A name draw does not make a character's background plausible by itself.

## Sources for given names

- U.S. Social Security Administration, [Top names of the 1990s](https://www.ssa.gov/OACT/babynames/decades/names1990s.html), for school-age names and ranks.
- U.S. Social Security Administration, [Top names of the 1970s](https://www.ssa.gov/oact/babynames/decades/names1970s.html), for adult community contacts near Claire's age.
- U.S. Social Security Administration, [Top names of the 1960s](https://www.ssa.gov/OACT/babynames/decades/names1960s.html), for the two middle-aged coaches.

SSA frequency data is a guide, not proof of a person's ethnicity, family history, personality or cultural identity.

## School-age male name draw

**Seed:** 98261012  
**Method:** Python random.Random(seed).sample(filtered_pool, 28), after freezing the rank-ordered candidate pool and filtering current canon names, registered names, rejected names and close/confusing variants.  
**Source:** SSA 1990s table, ranks 101–200; pool follows source order after filters.  
**Pool size:** 92. Exact candidate pool:

~~~text
Tanner, Angel, Vincent, Isaiah, Dalton, Brett, George, Alejandro, Elijah, Cory,
Cole, Joel, Erik, Jake, Mason, Jorge, Dillon, Raymond, Colton, Ricardo, Casey,
Brendan, Devon, Keith, Colin, Wesley, Oscar, Julian, Johnathan, Eduardo, Chad,
Bryce, Ronald, Alec, Dominic, Grant, Martin, Henry, Mario, Xavier, Manuel, Alan,
Derrick, Frank, Tristan, Collin, Omar, Jeremiah, Jackson, Troy, Edgar, Javier,
Douglas, Clayton, Jonathon, Nicolas, Andre, Ivan, Levi, Sergio, Roberto, Darius,
Andres, Cristian, Hector, Fernando, Curtis, Gary, Riley, Johnny, Dennis, Malik,
Wyatt, Cesar, Edwin, Gavin, Preston, Marco, Allen, Ruben, Calvin, Mathew, Randy,
Brent, Jerry, Hayden, Parker, Brady, Tony, Pedro, Craig, Larry
~~~

**Draw order returned by the seeded sample:**

1. Tristan — rank 148
2. Tanner — rank 101
3. Colton — rank 119
4. Brady — rank 196
5. Alec — rank 137
6. Calvin — rank 188
7. Chad — rank 133
8. Andres — rank 168
9. Elijah — rank 109
10. Xavier — rank 143
11. Ruben — rank 187
12. Marco — rank 185
13. Devon — rank 124
14. Johnny — rank 176
15. Omar — rank 150
16. Fernando — rank 171
17. Hector — rank 170
18. Javier — rank 155
19. Derrick — rank 146
20. Larry — rank 200
21. Mason — rank 115
22. Cory — rank 110
23. Mario — rank 142
24. Andre — rank 160
25. Alejandro — rank 108
26. Allen — rank 186
27. Cesar — rank 181
28. Wesley — rank 127

These are WORKING name assignments in the roster/social-circle files. Nathan and Maxwell keep their already established names and are not rerolled.

## School-age female name draw

The same seeded generator was used after the male sample. The next call was sample(female_pool, 5).  
**Source:** SSA 1990s table, ranks 101–200.  
**Pool size:** 95. Exact source-order pool:

~~~text
Bailey, Christine, Meghan, Lindsay, Angelica, Cynthia, Margaret, Kaitlin, Veronica,
Melanie, Bianca, Autumn, Ariel, Kristin, Bethany, Lisa, Kristina, Holly, Leslie,
Casey, Chloe, April, Julie, Kaylee, Brenda, Kathleen, Karen, Rachael, Sophia,
Patricia, Gabriela, Kendra, Dominique, Ana, Kara, Desiree, Tara, Michaela, Brandi,
Carly, Kylie, Karina, Adriana, Valerie, Caitlyn, Hayley, Rebekah, Jocelyn, Cassidy,
Jade, Gabriella, Makayla, Daisy, Alison, Jillian, Audrey, Faith, Nancy, Dana, Krystal,
Alejandra, Ariana, Summer, Isabella, Mikayla, Raven, Katrina, Kiara, Sandra, Meagan,
Lydia, Kirsten, Chelsey, Zoe, Monique, Claudia, Mallory, Joanna, Deanna, Isabel,
Ashlee, Felicia, Marisa, Mercedes, Mckenzie, Jasmin, Krista, Yesenia, Diamond, Evelyn,
Selena, Cindy, Brandy, Gina, Mia
~~~

**Selected:** Cynthia (rank 106), Kaitlin (rank 108), Desiree (rank 139), Kristina (rank 119), Julie (rank 125). Their character functions were allocated from the resulting sample; names are not locked.

## Adult community-contact draw

**Seed:** 63760112  
**Pool:** a frozen source-order shortlist from SSA 1970s female ranks 101–124 after canon/duplicate/rejection filters:

~~~text
Margaret, Victoria, Cindy, Jodi, Natalie, Brandi, Kristi, Suzanne, Samantha, Beth,
Tracey, Regina, Vanessa, Kristy, Carolyn, Yolanda, Deanna, Carla, Sheila, Laurie,
Anne, Shelly, Diane, Sabrina
~~~

**Method:** Python random.Random(seed).sample(pool, 3)  
**Selected:** Tracey (rank 111), Victoria (rank 102), Vanessa (rank 113).  
**Assigned working surnames:** Wheeler, Hutchinson, Quinn.

## Coach given-name draw

**Seed:** 63760113  
**Source:** SSA 1960s male ranks 101–200, with current canon/registered/confusable names filtered from the candidate pool. Exact frozen filtered pool:

~~~text
Albert, Darren, Ronnie, Ralph, Joel, Louis, Jim, Micheal, Marc, Frederick, Eddie,
Lee, Stanley, Tommy, Eugene, Tom, Tracy, Howard, Leonard, Kurt, Marvin, Kelly,
Brent, Ernest, Dwayne, Aaron, Rick, Benjamin, Bill, Reginald, Duane, Juan, Fred,
Melvin, Adam, Norman, Dan, Harry, Carlos, Nicholas, Jerome, Kirk, Ray, Don, Glen,
Brad, Theodore, Karl, Earl, Lance, Francis, Kent, Derek, Alfred, Antonio, Warren,
Clarence, Bernard, Kyle, Tyrone, Manuel, Luis, Gordon, Dave, Guy, Kerry, Daryl,
Leroy, Perry, Lonnie, Erik, Maurice, Marcus, Alvin, Gilbert, Vernon, Alexander,
Stuart, Rickey, Shane, Franklin, Leon, Gregg, Bob, Darin, Leslie, Gene, Herbert
~~~

**Method:** Python random.Random(seed).sample(pool, 2)  
**Selected:** Leonard (Seattle coach), Lance (Southern California coach).  
**Assigned working surnames:** Holloway and Conley.

## Working surname draw

Surname assignment used a separately frozen candidate pool to reduce name reuse. A first validation pass checked the assigned names against the displayed 2020 U.S. Census top-1,000 surname table reproduced by Behind the Name, which identifies the U.S. Census Bureau as its data source. The official Census Bureau page provides both the top-1,000 file and a complete file of 156,621 surnames; five assigned surnames were not found by searching the displayed top-1,000 page, so their exact status/rank in the full dataset remains unverified. All surnames remain WORKING and none is evidence of ancestry or an author-locked choice. Sources: [official 2020 Census names data](https://www.census.gov/topics/population/genealogy/data/2020_names.html); [2020 U.S. Census top-surname table](https://surnames.behindthename.com/top/lists/united-states/2020?display=max&sort=rank).

**Seed:** 98261013  
**Method:** Python random.Random(seed).sample(sorted(pool), 38).

Alphabetized candidate pool:

~~~text
Abbott, Baldwin, Barlow, Barrett, Baxter, Benson, Blevins, Cannon, Carver, Conley,
Cross, Doyle, Dunn, Fletcher, Flynn, Foster, Greer, Hale, Hendrix, Henson, Hodge,
Holloway, Hutchinson, Kendall, Keller, Kramer, Landry, Lawson, McBride, Mercer,
Merritt, Morrow, Moss, Perry, Phelps, Pratt, Pruitt, Quinn, Reeves, Rios,
Shepherd, Sloan, Stanton, Sutton, Vance, Vaughn, Wallace, Welch, Wheeler, Whitfield
~~~

Selected surname order:

~~~text
Morrow, Kramer, Shepherd, Vaughn, Reeves, Baxter, Pruitt, Phelps, Perry, Mercer,
Henson, Sloan, Carver, Sutton, Stanton, Merritt, Foster, Fletcher, Hendrix, Rios,
Baldwin, McBride, Abbott, Pratt, Lawson, Keller, Hodge, Holloway, Conley, Barrett,
Cannon, Vance, Barlow, Kendall, Wheeler, Hutchinson, Quinn, Moss
~~~

Assignment order:
- Seattle team: first 14 school-age male names use surname slots 1–14.
- California team: school-age male names 15–27 use surname slots 15–27.
- Coach names use surname slots 28–29.
- Alex/Haley school circles use surname slots 30–34, plus the separate established name Maxwell Whitaker.
- Claire's community circle uses surname slots 35–37.
- Wesley Moss uses surname slot 38.

This is a reproducibility trail, not a claim that every generated name must remain. If the author dislikes a name or a later character's birthplace/cohort makes it unsuitable, retain the old draw in the log, mark the rejected name RETIRED, make a reasoned change and rerun dependencies rather than silently swapping it.


## 2020 Census surname validation pass — partial results

**Method:** matched the assigned surnames against the 2020 U.S. Census top-1,000 table at the source above. The table reports one-based ranks. This pass confirms the entries actually returned by that table/search, rather than inferring missing ranks. “Unverified” means the displayed top-1,000 page search did not return a match; it does **not** prove that the surname is absent from the official complete dataset or establish a rank above 1,000.

| Assigned surname | Displayed 2020 rank | Validation status |
|---|---:|---|
| Morrow | 609 | Verified in top-1,000 table |
| Kramer | 547 | Verified in top-1,000 table |
| Shepherd | 552 | Verified in top-1,000 table |
| Vaughn | 370 | Verified in top-1,000 table |
| Reeves | 399 | Verified in top-1,000 table |
| Baxter | 712 | Verified in top-1,000 table |
| Pruitt | 801 | Verified in top-1,000 table |
| Phelps | 664 | Verified in top-1,000 table |
| Perry | 109 | Verified in top-1,000 table |
| Mercer | — | Not returned by displayed-page search; full-dataset rank unverified |
| Henson | 741 | Verified in top-1,000 table |
| Sloan | 808 | Verified in top-1,000 table |
| Carver | — | Not returned by displayed-page search; full-dataset rank unverified |
| Sutton | 351 | Verified in top-1,000 table |
| Stanton | 997 | Verified in top-1,000 table |
| Merritt | 772 | Verified in top-1,000 table |
| Foster | 104 | Verified in top-1,000 table |
| Fletcher | 397 | Verified in top-1,000 table |
| Hendrix | — | Not returned by displayed-page search; full-dataset rank unverified |
| Rios | 233 | Verified in top-1,000 table |
| Baldwin | 411 | Verified in top-1,000 table |
| McBride | 535 | Verified in top-1,000 table |
| Abbott | 661 | Verified in top-1,000 table |
| Pratt | 558 | Verified in top-1,000 table |
| Lawson | 267 | Verified in top-1,000 table |
| Keller | 329 | Verified in top-1,000 table |
| Hodge | 655 | Verified in top-1,000 table |
| Holloway | 585 | Verified in top-1,000 table |
| Conley | 622 | Verified in top-1,000 table |
| Barrett | 325 | Verified in top-1,000 table |
| Cannon | 480 | Verified in top-1,000 table |
| Vance | 754 | Verified in top-1,000 table |
| Barlow | — | Not returned by displayed-page search; full-dataset rank unverified |
| Kendall | — | Not returned by displayed-page search; full-dataset rank unverified |
| Wheeler | 254 | Verified in top-1,000 table |
| Hutchinson | 737 | Verified in top-1,000 table |
| Quinn | 429 | Verified in top-1,000 table |
| Moss | 436 | Verified in top-1,000 table |
| Whitaker (Maxwell) | 610 | Verified in top-1,000 table |

**Result:** 34 of the 39 assigned-surname uses are linked to an explicit top-1,000 rank in this pass (Whitaker is an existing separately assigned name); five distinct working surnames remain unverified in the full dataset: Mercer, Carver, Hendrix, Barlow and Kendall. Do not replace names solely to make the validation table appear complete. Revisit them only if a character becomes narratively important, the full dataset becomes directly accessible, or another source contradicts a name's suitability.

A frequency rank is not evidence of a particular character's ancestry, ethnicity, religion or family history. Cultural background must be separately designed and justified only if the story needs it.
