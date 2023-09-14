# Analysis on Indian Football data
## Task

In this task, we aim to extract the state of the birthplaces of different professional Indian football players who had and are playing for the country. For this purpose, we first scrapped information from the National Football teams Website. Please click [here](https://www.national-football-teams.com/) to visit the website. The code for scraping is available in the scraping.py file. Our main objective was to find the cumulative number of players in each state who were part of the National Squad. Note that, one player can be present in multiple years. We don't drop this players as they contribute to the statistical calculations in each individual year. To this end, we have created three choropleth maps of players from 2002-2013, 2014-2019 and 2021-2023, repectively. There was no data available for 2020. Below we provide the final table of the players and their respective birthplaces and states ordered over the years.  

## Table

| Year | Name                     | Birth Place        | State             |
|------|--------------------------|--------------------|-------------------|
| 2002 | Rajat Ghosh Dastidar     | Kolkata            | WEST BENGAL       |
| 2002 | Sangram Mukherjee        | Kolkata            | WEST BENGAL       |
| 2002 | Mahesh Gawli             | Panzorconi         | GOA               |
| 2002 | Deepak Kumar Mondal      | Noamundi           | WEST BENGAL       |
| 2002 | Samir Subash Naik        | Mumbai             | MAHARASHTRA       |
| 2002 | Satish Kumar Bharti      | Patna              | BIHAR             |
| 2002 | Debjit Ghosh             | Kolkata            | WEST BENGAL       |
| 2002 | Arun Kumar Malhotra      | Jammu & Kashmir    | JAMMU AND KASHMIR |
| 2002 | Renedy Singh             | Imphal             | MANIPUR           |
| 2002 | Shanmugham Venkatesh     | Bengaluru          | KARNATAKA         |
| 2002 | Tomba Singh              | Imphal             | MANIPUR           |
| 2002 | Jo Paul Ancheri          | Thrissur           | KERALA            |
| 2002 | Manitombi Singh          | Imphal             | MANIPUR           |
| 2002 | Krishnan Nair Ajayan     | Chadayamangalam    | KERALA            |
| 2002 | Baichung Bhutia          | Tinkitam           | SIKKIM            |
| 2002 | Abhishek Yadav           | Kanpur             | UTTAR PRADESH     |
| 2002 | Mutum Bijen Singh        | Imphal             | MANIPUR           |
| 2003 | Rajat Ghosh Dastidar     | Kolkata            | WEST BENGAL       |
| 2003 | Sangram Mukherjee        | Kolkata            | WEST BENGAL       |
| 2003 | Samir Subash Naik        | Mumbai             | MAHARASHTRA       |
| 2003 | Debjit Ghosh             | Kolkata            | WEST BENGAL       |
| 2003 | Mahesh Gawli             | Panzorconi         | GOA               |
| 2003 | Deepak Kumar Mondal      | Noamundi           | WEST BENGAL       |
| 2003 | Selwyn Fernandes         | Chinchinim         | GOA               |
| 2003 | Satish Kumar Bharti      | Patna              | BIHAR             |
| 2003 | Arun Kumar Malhotra      | Jammu & Kashmir    | JAMMU AND KASHMIR |
| 2003 | Jo Paul Ancheri          | Thrissur           | KERALA            |
| 2003 | Climax Lawrence          | Margao             | GOA               |
| 2003 | Renedy Singh             | Imphal             | MANIPUR           |
| 2003 | Shanmugham Venkatesh     | Bengaluru          | KARNATAKA         |
| 2003 | Tomba Singh              | Imphal             | MANIPUR           |
| 2003 | Jatin Singh Bisht        | Nainital           | UTTARAKHAND       |
| 2003 | Invalappil Mani Vijayan  | Thrissur           | KERALA            |
| 2003 | Abhishek Yadav           | Kanpur             | UTTAR PRADESH     |
| 2003 | Alvito D'Cunha           | Sanvordem          | GOA               |
| 2003 | Ashim Biswas             | Kolkata            | WEST BENGAL       |
| 2003 | Subhash Chakraborty      | Kolkata            | WEST BENGAL       |
| 2003 | Alex Ambrose             | Margao             | GOA               |
| 2003 | Baichung Bhutia          | Tinkitam           | SIKKIM            |
| 2004 | Sangram Mukherjee        | Kolkata            | WEST BENGAL       |
| 2004 | Sandip Nandy             | Burdwan            | WEST BENGAL       |
| 2004 | Deepak Kumar Mondal      | Noamundi           | WEST BENGAL       |
| 2004 | Samir Subash Naik        | Mumbai             | MAHARASHTRA       |
| 2004 | Mahesh Gawli             | Panzorconi         | GOA               |
| 2004 | Debabrata Roy            | Kolkata            | WEST BENGAL       |
| 2004 | Habibur Rehman Mondal    | Calcutta           | WEST BENGAL       |
| 2004 | Debjit Ghosh             | Kolkata            | WEST BENGAL       |
| 2004 | Vinu Jose                | Thiruvananthapuram | KERALA            |
| 2004 | Syed Rahim Nabi          | Pandua             | WEST BENGAL       |
| 2004 | Satish Kumar Bharti      | Patna              | BIHAR             |
| 2004 | Gurjinder Singh          | Gurdaspur          | PUNJAB            |
| 2004 | Climax Lawrence          | Margao             | GOA               |
| 2004 | Shanmugham Venkatesh     | Bengaluru          | KARNATAKA         |
| 2004 | Renedy Singh             | Imphal             | MANIPUR           |
| 2004 | Jatin Singh Bisht        | Nainital           | UTTARAKHAND       |
| 2004 | Jo Paul Ancheri          | Thrissur           | KERALA            |
| 2004 | Tomba Singh              | Imphal             | MANIPUR           |
| 2004 | Rocus Lamare             | Shillong           | MEGHALAYA         |
| 2004 | Steven Dias              | Mumbai             | MAHARASHTRA       |
| 2004 | Abhishek Yadav           | Kanpur             | UTTAR PRADESH     |
| 2004 | Baichung Bhutia          | Tinkitam           | SIKKIM            |
| 2004 | Ashim Biswas             | Kolkata            | WEST BENGAL       |
| 2004 | Alvito D'Cunha           | Sanvordem          | GOA               |
| 2004 | Jerry Zirsanga           | Aizwal             | MIZORAM           |
| 2004 | Mutum Bijen Singh        | Imphal             | MANIPUR           |
| 2004 | Subhash Chakraborty      | Kolkata            | WEST BENGAL       |
| 2005 | Sandip Nandy             | Burdwan            | WEST BENGAL       |
| 2005 | Irrungbam Surkumar Singh | Imphal             | MANIPUR           |
| 2005 | Mahesh Gawli             | Panzorconi         | GOA               |
| 2005 | Manju Shivananju         | Mysore             | KARNATAKA         |
| 2005 | Syed Rahim Nabi          | Pandua             | WEST BENGAL       |
| 2005 | Habibur Rehman Mondal    | Calcutta           | WEST BENGAL       |
| 2005 | Selwyn Fernandes         | Chinchinim         | GOA               |
| 2005 | Debabrata Roy            | Kolkata            | WEST BENGAL       |
| 2005 | Philip Gomes             | Margao             | GOA               |
| 2005 | Climax Lawrence          | Margao             | GOA               |
| 2005 | Shanmugham Venkatesh     | Bengaluru          | KARNATAKA         |
| 2005 | Krishnan Nair Ajayan     | Chadayamangalam    | KERALA            |
| 2005 | Mehtab Hossain           | Madhyamgram        | WEST BENGAL       |
| 2005 | Clifford Miranda Rayes   | Margao             | GOA               |
| 2005 | Mehrajuddin Wadoo        | Srinagar           | JAMMU AND KASHMIR |
| 2005 | Steven Dias              | Mumbai             | MAHARASHTRA       |
| 2005 | Shylo Malswama Tulunga   | Aizwal             | MANIPUR           |
| 2005 | N.P. Pradeep             | Idukki             | KERALA            |
| 2005 | Jatin Singh Bisht        | Nainital           | UTTARAKHAND       |
| 2005 | Sukhwinder Singh         | Nawanshahr         | PUNJAB            |
| 2005 | Bibiano Fernandes        | Mapusa             | GOA               |
| 2005 | Sunil Chhetri            | Secunderabad       | ANDHRA PRADESH    |
| 2005 | Baichung Bhutia          | Tinkitam           | SIKKIM            |
| 2005 | Abhishek Yadav           | Kanpur             | UTTAR PRADESH     |
| 2005 | Manjit Singh             | Gurdaspur          | PUNJAB            |
| 2005 | Alvito D'Cunha           | Sanvordem          | GOA               |
| 2005 | Surojit Bose             | Kolkata            | WEST BENGAL       |
| 2005 | Subhash Chakraborty      | Kolkata            | WEST BENGAL       |
| 2006 | Sandip Nandy             | Burdwan            | WEST BENGAL       |
| 2006 | Irrungbam Surkumar Singh | Imphal             | MANIPUR           |
| 2006 | Manju Shivananju         | Mysore             | KARNATAKA         |
| 2006 | Syed Rahim Nabi          | Pandua             | WEST BENGAL       |
| 2006 | Sanjeev Kumar Maria      | Chandigarh         | CHANDIGARH        |
| 2006 | Deepak Kumar Mondal      | Noamundi           | WEST BENGAL       |
| 2006 | Mahesh Gawli             | Panzorconi         | GOA               |
| 2006 | Anupam Sarkar            | Kolkata            | WEST BENGAL       |
| 2006 | Debabrata Roy            | Kolkata            | WEST BENGAL       |
| 2006 | Gouramangi Singh         | Imphal             | MANIPUR           |
| 2006 | Habibur Rehman Mondal    | Calcutta           | WEST BENGAL       |
| 2006 | Narinder Singh           | Hoshiarpur         | PUNJAB            |
| 2006 | Samir Subash Naik        | Mumbai             | MAHARASHTRA       |
| 2006 | N.P. Pradeep             | Idukki             | KERALA            |
| 2006 | Mehrajuddin Wadoo        | Srinagar           | JAMMU AND KASHMIR |
| 2006 | Steven Dias              | Mumbai             | MAHARASHTRA       |
| 2006 | Mehtab Hossain           | Madhyamgram        | WEST BENGAL       |
| 2006 | Renedy Singh             | Imphal             | MANIPUR           |
| 2006 | Krishnan Nair Ajayan     | Chadayamangalam    | KERALA            |
| 2006 | Shanmugham Venkatesh     | Bengaluru          | KARNATAKA         |
| 2006 | Micky Fernandes          | Goa                | GOA               |
| 2006 | Sampath Kuttimani        | Bengaluru          | KARNATAKA         |
| 2006 | Dharamjit Singh          | Imphal             | MANIPUR           |
| 2006 | Bungo Thomchok Singh     | Imphal             | MANIPUR           |
| 2006 | Baichung Bhutia          | Tinkitam           | SIKKIM            |
| 2006 | Manjit Singh             | Gurdaspur          | PUNJAB            |
| 2006 | Alvito D'Cunha           | Sanvordem          | GOA               |
| 2006 | Sunil Chhetri            | Secunderabad       | ANDHRA PRADESH    |
| 2007 | Subrata Pal              | Panihati           | WEST BENGAL       |
| 2007 | Sandip Nandy             | Burdwan            | WEST BENGAL       |
| 2007 | Mahesh Gawli             | Panzorconi         | GOA               |
| 2007 | Irrungbam Surkumar Singh | Imphal             | MANIPUR           |
| 2007 | Manju Shivananju         | Mysore             | KARNATAKA         |
| 2007 | Gouramangi Singh         | Imphal             | MANIPUR           |
| 2007 | Deepak Kumar Mondal      | Noamundi           | WEST BENGAL       |
| 2007 | Samir Subash Naik        | Mumbai             | MAHARASHTRA       |
| 2007 | Syed Rahim Nabi          | Pandua             | WEST BENGAL       |
| 2007 | Steven Dias              | Mumbai             | MAHARASHTRA       |
| 2007 | Climax Lawrence          | Margao             | GOA               |
| 2007 | N.P. Pradeep             | Idukki             | KERALA            |
| 2007 | Renedy Singh             | Imphal             | MANIPUR           |
| 2007 | Krishnan Nair Ajayan     | Chadayamangalam    | KERALA            |
| 2007 | Clifford Miranda Rayes   | Margao             | GOA               |
| 2007 | Mehrajuddin Wadoo        | Srinagar           | JAMMU AND KASHMIR |
| 2007 | Sunil Chhetri            | Secunderabad       | ANDHRA PRADESH    |
| 2007 | Baichung Bhutia          | Tinkitam           | SIKKIM            |
| 2007 | Abhishek Yadav           | Kanpur             | UTTAR PRADESH     |
| 2008 | Subrata Pal              | Panihati           | WEST BENGAL       |
| 2008 | Subhasish Roy Chowdhury  | Kolkata            | WEST BENGAL       |
| 2008 | Gouramangi Singh         | Imphal             | MANIPUR           |
| 2008 | Anwar Ali                | Rurka Kalan        | PUNJAB            |
| 2008 | Deepak Kumar Mondal      | Noamundi           | WEST BENGAL       |
| 2008 | Samir Subash Naik        | Mumbai             | MAHARASHTRA       |
| 2008 | Mahesh Gawli             | Panzorconi         | GOA               |
| 2008 | Irrungbam Surkumar Singh | Imphal             | MANIPUR           |
| 2008 | Manju Shivananju         | Mysore             | KARNATAKA         |
| 2008 | Syed Rahim Nabi          | Pandua             | WEST BENGAL       |
| 2008 | Climax Lawrence          | Margao             | GOA               |
| 2008 | N.P. Pradeep             | Idukki             | KERALA            |
| 2008 | Renedy Singh             | Imphal             | MANIPUR           |
| 2008 | Steven Dias              | Mumbai             | MAHARASHTRA       |
| 2008 | Bungo Thomchok Singh     | Imphal             | MANIPUR           |
| 2008 | Mehrajuddin Wadoo        | Srinagar           | JAMMU AND KASHMIR |
| 2008 | Clifford Miranda Rayes   | Margao             | GOA               |
| 2008 | Sampath Kuttimani        | Bengaluru          | KARNATAKA         |
| 2008 | Baldeep Singh            | Hoshiarpur         | PUNJAB            |
| 2008 | Krishnan Nair Ajayan     | Chadayamangalam    | KERALA            |
| 2008 | Sunil Chhetri            | Secunderabad       | ANDHRA PRADESH    |
| 2008 | Baichung Bhutia          | Tinkitam           | SIKKIM            |
| 2008 | Sushil Kumar Singh       | Manipur            | MANIPUR           |
| 2008 | Manjit Singh             | Gurdaspur          | PUNJAB            |
| 2008 | Abhishek Yadav           | Kanpur             | UTTAR PRADESH     |
| 2009 | Subrata Pal              | Panihati           | WEST BENGAL       |
| 2009 | Gouramangi Singh         | Imphal             | MANIPUR           |
| 2009 | Anwar Ali                | Rurka Kalan        | PUNJAB            |
| 2009 | Mahesh Gawli             | Panzorconi         | GOA               |
| 2009 | Deepak Kumar Mondal      | Noamundi           | WEST BENGAL       |
| 2009 | Irrungbam Surkumar Singh | Imphal             | MANIPUR           |
| 2009 | Syed Rahim Nabi          | Pandua             | WEST BENGAL       |
| 2009 | Samir Subash Naik        | Mumbai             | MAHARASHTRA       |
| 2009 | Manju Shivananju         | Mysore             | KARNATAKA         |
| 2009 | Climax Lawrence          | Margao             | GOA               |
| 2009 | Steven Dias              | Mumbai             | MAHARASHTRA       |
| 2009 | N.P. Pradeep             | Idukki             | KERALA            |
| 2009 | Anthony Pereira          | Goa                | GOA               |
| 2009 | Mehrajuddin Wadoo        | Srinagar           | JAMMU AND KASHMIR |
| 2009 | Renedy Singh             | Imphal             | MANIPUR           |
| 2009 | Rakesh Masih             | Ballowal           | PUNJAB            |
| 2009 | Baichung Bhutia          | Tinkitam           | SIKKIM            |
| 2009 | Sunil Chhetri            | Secunderabad       | ANDHRA PRADESH    |
| 2009 | Sushil Kumar Singh       | Manipur            | MANIPUR           |
| 2009 | Abhishek Yadav           | Kanpur             | UTTAR PRADESH     |
| 2010 | Subrata Pal              | Panihati           | WEST BENGAL       |
| 2010 | Karanjit Singh           | Hoshiarpur         | PUNJAB            |
| 2010 | Irrungbam Surkumar Singh | Imphal             | MANIPUR           |
| 2010 | Anwar Ali                | Rurka Kalan        | PUNJAB            |
| 2010 | Gouramangi Singh         | Imphal             | MANIPUR           |
| 2010 | Syed Rahim Nabi          | Pandua             | WEST BENGAL       |
| 2010 | Mahesh Gawli             | Panzorconi         | GOA               |
| 2010 | Deepak Kumar Mondal      | Noamundi           | WEST BENGAL       |
| 2010 | Manju Shivananju         | Mysore             | KARNATAKA         |
| 2010 | Denzil Franco            | Saligao            | GOA               |
| 2010 | Jibon Singh              | Imphal             | MANIPUR           |
| 2010 | Nirmal Chettri           | Sikkim             | SIKKIM            |
| 2010 | Rowilson Rodrigues       | Goa                | GOA               |
| 2010 | Debabrata Roy            | Kolkata            | WEST BENGAL       |
| 2010 | Gurwinder Singh          | Jalandhar          | PUNJAB            |
| 2010 | Robert Lalthlamuana      | Margao             | GOA               |
| 2010 | Dharmaraj Ravanan        | Tiruchirappalli    | TAMIL NADU        |
| 2010 | Anthony Pereira          | Goa                | GOA               |
| 2010 | Climax Lawrence          | Margao             | GOA               |
| 2010 | Clifford Miranda Rayes   | Margao             | GOA               |
| 2010 | Steven Dias              | Mumbai             | MAHARASHTRA       |
| 2010 | N.P. Pradeep             | Idukki             | KERALA            |
| 2010 | Mehrajuddin Wadoo        | Srinagar           | JAMMU AND KASHMIR |
| 2010 | Baldeep Singh            | Hoshiarpur         | PUNJAB            |
| 2010 | Rakesh Masih             | Ballowal           | PUNJAB            |
| 2010 | Renedy Singh             | Imphal             | MANIPUR           |
| 2010 | Baljit Singh Sahni       | Hoshiarpur         | PUNJAB            |
| 2010 | Jewel Raja Shaikh        | Budge Budge        | WEST BENGAL       |
| 2010 | Lalrindika Ralte         | Lunglei            | MIZORAM           |
| 2010 | Sunil Chhetri            | Secunderabad       | ANDHRA PRADESH    |
| 2010 | Abhishek Yadav           | Kanpur             | UTTAR PRADESH     |
| 2010 | Sushil Kumar Singh       | Manipur            | MANIPUR           |
| 2010 | Mohammed Rafi            | Kasaragod          | KERALA            |
| 2010 | Baichung Bhutia          | Tinkitam           | SIKKIM            |
| 2010 | Jeje Lalpekhlua          | Hnahthial          | MIZORAM           |
| 2010 | Joaquim Abranches        | Verna              | GOA               |
| 2010 | Balwant Singh            | Hoshiarpur         | PUNJAB            |
| 2010 | Jagtar Singh             | Hoshiarpur         | PUNJAB            |
| 2011 | Subrata Pal              | Panihati           | WEST BENGAL       |
| 2011 | Karanjit Singh           | Hoshiarpur         | PUNJAB            |
| 2011 | Subhasish Roy Chowdhury  | Kolkata            | WEST BENGAL       |
| 2011 | Gurpreet Singh Sandhu    | Chamkaur           | PUNJAB            |
| 2011 | Syed Rahim Nabi          | Pandua             | WEST BENGAL       |
| 2011 | Gouramangi Singh         | Imphal             | MANIPUR           |
| 2011 | Mahesh Gawli             | Panzorconi         | GOA               |
| 2011 | Raju Gaikwad             | Mumbai             | MAHARASHTRA       |
| 2011 | Samir Subash Naik        | Mumbai             | MAHARASHTRA       |
| 2011 | Anwar Ali                | Rurka Kalan        | PUNJAB            |
| 2011 | Debabrata Roy            | Kolkata            | WEST BENGAL       |
| 2011 | Nirmal Chettri           | Sikkim             | SIKKIM            |
| 2011 | Govin Singh              | Tentha             | MANIPUR           |
| 2011 | Irrungbam Surkumar Singh | Imphal             | MANIPUR           |
| 2011 | Manju Shivananju         | Mysore             | KARNATAKA         |
| 2011 | Deepak Kumar Mondal      | Noamundi           | WEST BENGAL       |
| 2011 | Denzil Franco            | Saligao            | GOA               |
| 2011 | Nallappan Mohanraj       | Namakkal           | TAMIL NADU        |
| 2011 | Jaspal Singh             | Hoshiarpur         | PUNJAB            |
| 2011 | Robert Lalthlamuana      | Margao             | GOA               |
| 2011 | Valeriano Rebello        | Goa                | GOA               |
| 2011 | Rowilson Rodrigues       | Goa                | GOA               |
| 2011 | Climax Lawrence          | Margao             | GOA               |
| 2011 | Steven Dias              | Mumbai             | MAHARASHTRA       |
| 2011 | Clifford Miranda Rayes   | Margao             | GOA               |
| 2011 | Rocus Lamare             | Shillong           | MEGHALAYA         |
| 2011 | Mehtab Hossain           | Madhyamgram        | WEST BENGAL       |
| 2011 | Anthony Pereira          | Goa                | GOA               |
| 2011 | Jewel Raja Shaikh        | Budge Budge        | WEST BENGAL       |
| 2011 | N.P. Pradeep             | Idukki             | KERALA            |
| 2011 | Renedy Singh             | Imphal             | MANIPUR           |
| 2011 | Rakesh Masih             | Ballowal           | PUNJAB            |
| 2011 | Baldeep Singh            | Hoshiarpur         | PUNJAB            |
| 2011 | Jagpreet Singh           | Ludhiana           | PUNJAB            |
| 2011 | Lalrindika Ralte         | Lunglei            | MIZORAM           |
| 2011 | Shilton D'Silva          | Mumbai             | MAHARASHTRA       |
| 2011 | Francis Fernandes        | Margao             | GOA               |
| 2011 | Baljit Singh Sahni       | Hoshiarpur         | PUNJAB            |
| 2011 | Mehrajuddin Wadoo        | Srinagar           | JAMMU AND KASHMIR |
| 2011 | Peter Carvalho           | Quepem             | GOA               |
| 2011 | Harmanjot Khabra         | Garhshankar        | PUNJAB            |
| 2011 | Sunil Chhetri            | Secunderabad       | ANDHRA PRADESH    |
| 2011 | Jeje Lalpekhlua          | Hnahthial          | MIZORAM           |
| 2011 | Sushil Kumar Singh       | Manipur            | MANIPUR           |
| 2011 | Joaquim Abranches        | Verna              | GOA               |
| 2011 | Abhishek Yadav           | Kanpur             | UTTAR PRADESH     |
| 2011 | Chinadorai Sabeeth       | Chennai            | TAMIL NADU        |
| 2011 | Baichung Bhutia          | Tinkitam           | SIKKIM            |
| 2012 | Subrata Pal              | Panihati           | WEST BENGAL       |
| 2012 | Karanjit Singh           | Hoshiarpur         | PUNJAB            |
| 2012 | Subhasish Roy Chowdhury  | Kolkata            | WEST BENGAL       |
| 2012 | Gouramangi Singh         | Imphal             | MANIPUR           |
| 2012 | Syed Rahim Nabi          | Pandua             | WEST BENGAL       |
| 2012 | Raju Gaikwad             | Mumbai             | MAHARASHTRA       |
| 2012 | Nirmal Chettri           | Sikkim             | SIKKIM            |
| 2012 | Samir Subash Naik        | Mumbai             | MAHARASHTRA       |
| 2012 | Denzil Franco            | Saligao            | GOA               |
| 2012 | Gurjinder Kumar          | Nawanshahr         | PUNJAB            |
| 2012 | Gurjinder Singh          | Gurdaspur          | ASSAM             |
| 2012 | Anwar Ali                | Rurka Kalan        | PUNJAB            |
| 2012 | Francis Fernandes        | Margao             | GOA               |
| 2012 | Mehtab Hossain           | Madhyamgram        | WEST BENGAL       |
| 2012 | Clifford Miranda Rayes   | Margao             | GOA               |
| 2012 | Lenny Rodrigues          | Verna              | GOA               |
| 2012 | Sanju Pradhan            | Gangtok            | SIKKIM            |
| 2012 | Anthony Pereira          | Goa                | GOA               |
| 2012 | Jewel Raja Shaikh        | Budge Budge        | WEST BENGAL       |
| 2012 | Adil Khan                | Verna              | GOA               |
| 2012 | Rocus Lamare             | Shillong           | MEGHALAYA         |
| 2012 | Lester Fernandes         | Bengaluru          | KARNATAKA         |
| 2012 | Manish Maithani          | Dehradun           | HIMACHAL PRADESH  |
| 2012 | Baldeep Singh            | Hoshiarpur         | PUNJAB            |
| 2012 | Alwyn George             | Nagpur             | MAHARASHTRA       |
| 2012 | Lalrindika Ralte         | Lunglei            | MIZORAM           |
| 2012 | Sunil Chhetri            | Secunderabad       | ANDHRA PRADESH    |
| 2012 | Sushil Kumar Singh       | Manipur            | MANIPUR           |
| 2012 | Joaquim Abranches        | Verna              | GOA               |
| 2012 | Reisangmei Vashum        | Manipur            | MANIPUR           |
| 2012 | Manandeep Singh          | Hisar              | HARYANA           |
| 2012 | Robin Singh              | Noida              | "DELHI            |   |  " |
| 2012 | Chinadorai Sabeeth       | Chennai            | TAMIL NADU        |
| 2013 | Subrata Pal              | Panihati           | WEST BENGAL       |
| 2013 | Karanjit Singh           | Hoshiarpur         | PUNJAB            |
| 2013 | Sandip Nandy             | Burdwan            | WEST BENGAL       |
| 2013 | Gouramangi Singh         | Imphal             | MANIPUR           |
| 2013 | Arnab Mondal             | Behala             | WEST BENGAL       |
| 2013 | Nirmal Chettri           | Sikkim             | SIKKIM            |
| 2013 | Syed Rahim Nabi          | Pandua             | WEST BENGAL       |
| 2013 | Raju Gaikwad             | Mumbai             | MAHARASHTRA       |
| 2013 | Denzil Franco            | Saligao            | GOA               |
| 2013 | Gurjinder Kumar          | Nawanshahr         | PUNJAB            |
| 2013 | Nallappan Mohanraj       | Namakkal           | TAMIL NADU        |
| 2013 | Aiborlang Khongjee       | Lyngkhat           | MEGHALAYA         |
| 2013 | Narayan Das              | Jharkhand          | JHARKHAND         |
| 2013 | Mehtab Hossain           | Madhyamgram        | WEST BENGAL       |
| 2013 | Francis Fernandes        | Margao             | GOA               |
| 2013 | Lenny Rodrigues          | Verna              | GOA               |
| 2013 | Clifford Miranda Rayes   | Margao             | GOA               |
| 2013 | Jewel Raja Shaikh        | Budge Budge        | WEST BENGAL       |
| 2013 | Arata Izumi              | Japan              | NA                |
| 2013 | Alwyn George             | Nagpur             | MAHARASHTRA       |
| 2013 | Lalrindika Ralte         | Lunglei            | MIZORAM           |
| 2013 | C.K. Vineeth             | Kerala             | KERALA            |
| 2013 | Rocus Lamare             | Shillong           | MEGHALAYA         |
| 2013 | Shylo Malswama Tulunga   | Aizwal             | MIZORAM           |
| 2013 | Sunil Chhetri            | Secunderabad       | ANDHRA PRADESH    |
| 2013 | Jeje Lalpekhlua          | Hnahthial          | MIZORAM           |
| 2013 | Robin Singh              | Noida              | "DELHI            |   |  " |
| 2013 | Dawson Fernandes         | Margao             | GOA               |
| 2013 | Joaquim Abranches        | Verna              | GOA               |
| 2013 | Manandeep Singh          | Hisar              | HARYANA           |
| 2013 | Victorino Fernandes      | Goa                | GOA               |
| 2014 | Subrata Pal              | Panihati           | WEST BENGAL       |
| 2014 | Karanjit Singh           | Hoshiarpur         | PUNJAB            |
| 2014 | Denzil Franco            | Saligao            | GOA               |
| 2014 | Aiborlang Khongjee       | Lyngkhat           | MEGHALAYA         |
| 2014 | Arnab Mondal             | Behala             | WEST BENGAL       |
| 2014 | Narayan Das              | Jharkhand          | JHARKHAND         |
| 2014 | Raju Gaikwad             | Mumbai             | MAHARASHTRA       |
| 2014 | Francis Fernandes        | Margao             | GOA               |
| 2014 | Mehtab Hossain           | Madhyamgram        | WEST BENGAL       |
| 2014 | Clifford Miranda Rayes   | Margao             | GOA               |
| 2014 | Lenny Rodrigues          | Verna              | GOA               |
| 2014 | Alwyn George             | Nagpur             | MAHARASHTRA       |
| 2014 | Arata Izumi              | Japan              | NA                |
| 2014 | Rocus Lamare             | Shillong           | MEGHALAYA         |
| 2014 | Sunil Chhetri            | Secunderabad       | TELANGANA         |
| 2014 | Robin Singh              | Noida              | "DELHI            |   |  " |
| 2014 | Seminlen Doungel         | Manipur            | MANIPUR           |
| 2014 | Balwant Singh            | Hoshiarpur         | PUNJAB            |
| 2014 | Victorino Fernandes      | Goa                | GOA               |
| 2015 | Subrata Pal              | Panihati           | WEST BENGAL       |
| 2015 | Gurpreet Singh Sandhu    | Chamkaur           | PUNJAB            |
| 2015 | Karanjit Singh           | Hoshiarpur         | PUNJAB            |
| 2015 | Arnab Mondal             | Behala             | WEST BENGAL       |
| 2015 | Pritam Kotal             | Uttarpara          | WEST BENGAL       |
| 2015 | Narayan Das              | Jharkhand          | JHARKHAND         |
| 2015 | Sandesh Jhingan          | Chandigarh         | CHANDIGARH        |
| 2015 | Rino Anto                | Thrissur           | KERALA            |
| 2015 | Augustin Fernandes       | Goa                | GOA               |
| 2015 | Lalchhuanmawia Fanai     | Lengpui            | MIZORAM           |
| 2015 | Saumik Dey               | Hindmotor          | WEST BENGAL       |
| 2015 | Dhanachandra Singh       | Imphal             | MANIPUR           |
| 2015 | Aiborlang Khongjee       | Lyngkhat           | MEGHALAYA         |
| 2015 | Koushik Sarkar           | Chinsurah          | WEST BENGAL       |
| 2015 | Eugeneson Lyngdoh        | Shillong           | MEGHALAYA         |
| 2015 | Francis Fernandes        | Margao             | GOA               |
| 2015 | Sehnaj Singh             | Chandigarh         | CHANDIGARH        |
| 2015 | Rowllin Borges           | Nuvem              | GOA               |
| 2015 | Bikash Jairu             | Gyalshing          | SIKKIM            |
| 2015 | Pronay Halder            | Barrackpore        | WEST BENGAL       |
| 2015 | Cavin Lobo               | Goa                | GOA               |
| 2015 | Dhanpal Ganesh           | Chennai            | TAMIL NADU        |
| 2015 | Sanju Pradhan            | Sikkim             | SIKKIM            |
| 2015 | C.K. Vineeth             | Kerala             | KERALA            |
| 2015 | Lalrindika Ralte         | Lunglei            | MIZORAM           |
| 2015 | Lenny Rodrigues          | Verna              | GOA               |
| 2015 | Romeo Fernandes          | Assolna            | GOA               |
| 2015 | Harmanjot Khabra         | Garhshankar        | PUNJAB            |
| 2015 | Seityasen Singh          | Manipur            | MANIPUR           |
| 2015 | Sunil Chhetri            | Secunderabad       | TELANGANA         |
| 2015 | Robin Singh              | Noida              | "DELHI            |   |  " |
| 2015 | Jeje Lalpekhlua          | Hnahthial          | MIZORAM           |
| 2015 | Jackichand Singh         | Manipur            | MANIPUR           |
| 2015 | Holicharan Narzary       | Kokrajhar          | ASSAM             |
| 2015 | Lallianzuala Chhangte    | Mizoram            | MIZORAM           |
| 2016 | Gurpreet Singh Sandhu    | Chamkaur           | PUNJAB            |
| 2016 | Subrata Pal              | Panihati           | WEST BENGAL       |
| 2016 | Sandesh Jhingan          | Chandigarh         | CHANDIGARH        |
| 2016 | Narayan Das              | Jharkhand          | JHARKHAND         |
| 2016 | Arnab Mondal             | Behala             | WEST BENGAL       |
| 2016 | Pritam Kotal             | Uttarpara          | WEST BENGAL       |
| 2016 | Augustin Fernandes       | Goa                | GOA               |
| 2016 | Rino Anto                | Thrissur           | KERALA            |
| 2016 | Aiborlang Khongjee       | Lyngkhat           | MEGHALAYA         |
| 2016 | Keegan Pereira           | Mumbai             | MAHARASHTRA       |
| 2016 | Fulganco Cardozo         | Goa                | GOA               |
| 2016 | Lalchhuanmawia Fanai     | Lengpui            | MIZORAM           |
| 2016 | Koushik Sarkar           | Chinsurah          | WEST BENGAL       |
| 2016 | Chinglensana Singh       | Manipur            | MANIPUR           |
| 2016 | Eugeneson Lyngdoh        | Shillong           | MEGHALAYA         |
| 2016 | Rowllin Borges           | Nuvem              | GOA               |
| 2016 | Pronay Halder            | Barrackpore        | WEST BENGAL       |
| 2016 | Bikash Jairu             | Gyalshing          | SIKKIM            |
| 2016 | Mohammed Rafique         | Kolkata            | WEST BENGAL       |
| 2016 | Cavin Lobo               | Goa                | GOA               |
| 2016 | Seityasen Singh          | Manipur            | MANIPUR           |
| 2016 | Alwyn George             | Nagpur             | MAHARASHTRA       |
| 2016 | Germanpreet Singh        | Gurdaspur          | PUNJAB            |
| 2016 | Harmanjot Khabra         | Garhshankar        | PUNJAB            |
| 2016 | Sanju Pradhan            | Sikkim             | SIKKIM            |
| 2016 | Dhanpal Ganesh           | Chennai            | TAMIL NADU        |
| 2016 | Vinit Rai                | Assam              | ASSAM             |
| 2016 | Isaac Vanmalsawma        | Lunglei            | MIZORAM           |
| 2016 | Jeje Lalpekhlua          | Hnahthial          | MIZORAM           |
| 2016 | Sunil Chhetri            | Secunderabad       | TELANGANA         |
| 2016 | Udanta Singh             | Manipur            | MANIPUR           |
| 2016 | Holicharan Narzary       | Kokrajhar          | ASSAM             |
| 2016 | Sumeet Passi             | Ambala City        | HARYANA           |
| 2016 | Jackichand Singh         | Manipur            | MANIPUR           |
| 2016 | Daniel Lalhlimpuia       | Serchhip           | MIZORAM           |
| 2016 | Lallianzuala Chhangte    | Mizoram            | MIZORAM           |
| 2017 | Gurpreet Singh Sandhu    | Chamkaur           | PUNJAB            |
| 2017 | Subrata Pal              | Panihati           | WEST BENGAL       |
| 2017 | Amrinder Singh           | Manolian           | PUNJAB            |
| 2017 | Anas Edathodika          | Kondotty           | KERALA            |
| 2017 | Pritam Kotal             | Uttarpara          | WEST BENGAL       |
| 2017 | Sandesh Jhingan          | Chandigarh         | CHANDIGARH        |
| 2017 | Narayan Das              | Jharkhand          | JHARKHAND         |
| 2017 | Jerry Lalrinzuala        | Mizoram            | MIZORAM           |
| 2017 | Arnab Mondal             | Behala             | WEST BENGAL       |
| 2017 | Fulganco Cardozo         | Goa                | GOA               |
| 2017 | Salam Ranjan Singh       | Kha-Potessangbam   | MANIPUR           |
| 2017 | Eugeneson Lyngdoh        | Shillong           | MEGHALAYA         |
| 2017 | Rowllin Borges           | Nuvem              | GOA               |
| 2017 | Mohammed Rafique         | Kolkata            | WEST BENGAL       |
| 2017 | Germanpreet Singh        | Gurdaspur          | PUNJAB            |
| 2017 | C.K. Vineeth             | Kerala             | KERALA            |
| 2017 | Bikash Jairu             | Gyalshing          | SIKKIM            |
| 2017 | Nikhil Poojari           | Maharashtra        | MAHARASHTRA       |
| 2017 | Anirudh Thapa            | Dehradun           | HIMACHAL PRADESH  |
| 2017 | Dhanpal Ganesh           | Chennai            | TAMIL NADU        |
| 2017 | Milan Singh              | Manipur            | MANIPUR           |
| 2017 | Seityasen Singh          | Manipur            | MANIPUR           |
| 2017 | Jeje Lalpekhlua          | Hnahthial          | MIZORAM           |
| 2017 | Holicharan Narzary       | Kokrajhar          | ASSAM             |
| 2017 | Jackichand Singh         | Manipur            | MANIPUR           |
| 2017 | Sunil Chhetri            | Secunderabad       | TELANGANA         |
| 2017 | Robin Singh              | Noida              | "DELHI            |   |  " |
| 2017 | Udanta Singh             | Manipur            | MANIPUR           |
| 2017 | Balwant Singh            | Hoshiarpur         | PUNJAB            |
| 2017 | Daniel Lalhlimpuia       | Serchhip           | MIZORAM           |
| 2017 | Manvir Singh             | Duhre              | TAMIL NADU        |
| 2018 | Gurpreet Singh Sandhu    | Chamkaur           | PUNJAB            |
| 2018 | Vishal Kaith             | Himachal Pradesh   | HIMACHAL PRADESH  |
| 2018 | Amrinder Singh           | Manolian           | PUNJAB            |
| 2018 | Subhasish Bose           | Kolkata            | WEST BENGAL       |
| 2018 | Pritam Kotal             | Uttarpara          | WEST BENGAL       |
| 2018 | Salam Ranjan Singh       | Kha-Potessangbam   | MANIPUR           |
| 2018 | Anas Edathodika          | Kondotty           | KERALA            |
| 2018 | Sandesh Jhingan          | Chandigarh         | CHANDIGARH        |
| 2018 | Narayan Das              | Jharkhand          | JHARKHAND         |
| 2018 | Davinder Singh           | Betalghat          | UTTARAKHAND       |
| 2018 | Jerry Lalrinzuala        | Mizoram            | MIZORAM           |
| 2018 |  Lalruatthara            | Aizawl             | MIZORAM           |
| 2018 | Mohammad Sajid Dhot      | Punjab             | PUNJAB            |
| 2018 | Vignesh Dakshina Murthy  | Bengaluru          | KARNATAKA         |
| 2018 | Nishu Kumar              | Muzaffarnagar      | UTTAR PRADESH     |
| 2018 | Anirudh Thapa            | Dehradun           | HIMACHAL PRADESH  |
| 2018 | Pronay Halder            | Barrackpore        | WEST BENGAL       |
| 2018 | Vinit Rai                | Assam              | ASSAM             |
| 2018 | Nikhil Poojari           | Maharashtra        | MAHARASHTRA       |
| 2018 | Rowllin Borges           | Nuvem              | GOA               |
| 2018 | Germanpreet Singh        | Gurdaspur          | PUNJAB            |
| 2018 | Mohammed Rafique         | Kolkata            | WEST BENGAL       |
| 2018 | Hitesh Sharma            | Jalandhar          | PUNJAB            |
| 2018 | Jeje Lalpekhlua          | Hnahthial          | MIZORAM           |
| 2018 | Udanta Singh             | Manipur            | MANIPUR           |
| 2018 | Holicharan Narzary       | Kokrajhar          | ASSAM             |
| 2018 | Sunil Chhetri            | Secunderabad       | TELANGANA         |
| 2018 | Ashique Kuruniyan        | Malappuram         | KERALA            |
| 2018 | Farukh Choudhary         | Ambarnath          | MAHARASHTRA       |
| 2018 | Manvir Singh             | Duhre              | PUNJAB            |
| 2018 | Balwant Singh            | Hoshiarpur         | PUNJAB            |
| 2018 | Lallianzuala Chhangte    | Mizoram            | MIZORAM           |
| 2018 | Sumeet Passi             | Ambala City        | HARYANA           |
| 2018 | Jackichand Singh         | Manipur            | MANIPUR           |
| 2018 | Alen Deory               | Guwahati           | ASSAM             |
| 2018 | Seminlen Doungel         | Manipur            | MANIPUR           |
| 2018 | Laldanmawia Ralte        | Sialhawk           | MIZORAM           |
| 2019 | Gurpreet Singh Sandhu    | Chamkaur           | PUNJAB            |
| 2019 | Amrinder Singh           | Manolian           | PUNJAB            |
| 2019 | Rahul Bheke              | Mumbai             | MAHARASHTRA       |
| 2019 | Sandesh Jhingan          | Chandigarh         | CHANDIGARH        |
| 2019 | Subhasish Bose           | Kolkata            | WEST BENGAL       |
| 2019 | Pritam Kotal             | Uttarpara          | WEST BENGAL       |
| 2019 | Anas Edathodika          | Kondotty           | KERALA            |
| 2019 | Narender Gahlot          | Delhi              | "DELHI            |   |  " |
| 2019 | Jerry Lalrinzuala        | Mizoram            | MIZORAM           |
| 2019 | Nishu Kumar              | Muzaffarnagar      | UTTAR PRADESH     |
| 2019 | Salam Ranjan Singh       | Kha-Potessangbam   | MANIPUR           |
| 2019 | Anirudh Thapa            | Dehradun           | HIMACHAL PRADESH  |
| 2019 | Adil Khan                | Verna              | GOA               |
| 2019 | Sahal Abdul Samad        | Payyanur           | PUNJAB            |
| 2019 | Pronay Halder            | Barrackpore        | WEST BENGAL       |
| 2019 | Brandon Fernandes        | Margao             | GOA               |
| 2019 | Mandar Rao Dessai        | Mapusa             | GOA               |
| 2019 | Rowllin Borges           | Nuvem              | GOA               |
| 2019 | Amarjit Singh            | Thoubal            | MANIPUR           |
| 2019 | Vinit Rai                | Assam              | ASSAM             |
| 2019 | Raynier Fernandes        | Mumbai             | MAHARASHTRA       |
| 2019 | Nikhil Poojari           | Maharashtra        | MAHARASHTRA       |
| 2019 | Germanpreet Singh        | Gurdaspur          | PUNJAB            |
| 2019 | Michael Soosairaj        | Eraviputhenthurai  | TAMIL NADU        |
| 2019 | Udanta Singh             | Manipur            | MANIPUR           |
| 2019 | Sunil Chhetri            | Secunderabad       | TELANGANA         |
| 2019 | Ashique Kuruniyan        | Malappuram         | KERALA            |
| 2019 | Manvir Singh             | Duhre              | PUNJAB            |
| 2019 | Lallianzuala Chhangte    | Mizoram            | MIZORAM           |
| 2019 | Holicharan Narzary       | Kokrajhar          | ASSAM             |
| 2019 | Farukh Choudhary         | Ambarnath          | MAHARASHTRA       |
| 2019 | Jobby Justin             | Trivandrum         | KERALA            |
| 2019 | Balwant Singh            | Hoshiarpur         | PUNJAB            |
| 2019 | Jeje Lalpekhlua          | Hnahthial          | MIZORAM           |
| 2019 | Jackichand Singh         | Manipur            | MANIPUR           |
| 2019 | Seminlen Doungel         | Manipur            | MANIPUR           |
| 2021 | Gurpreet Singh Sandhu    | Chamkaur           | PUNJAB            |
| 2021 | Amrinder Singh           | Manolian           | PUNJAB            |
| 2021 | Subhasish Bose           | Kolkata            | WEST BENGAL       |
| 2021 | Rahul Bheke              | Mumbai             | MAHARASHTRA       |
| 2021 | Chinglensana Singh       | Manipur            | MANIPUR           |
| 2021 | Pritam Kotal             | Uttarpara          | WEST BENGAL       |
| 2021 | Sandesh Jhingan          | Chandigarh         | CHANDIGARH        |
| 2021 | Akash Mishra             | Balrampur          | UTTAR PRADESH     |
| 2021 | Seriton Fernandes        | Goa                | GOA               |
| 2021 | Ashutosh Mehta           | Mumbai             | MAHARASHTRA       |
| 2021 | Suresh Singh Wangjam     | Manipur            | MANIPUR           |
| 2021 | Glan Martins             | Goa                | GOA               |
| 2021 | Lalengmawia Ralte        | Aizawl             | MIZORAM           |
| 2021 | Anirudh Thapa            | Dehradun           | HIMACHAL PRADESH  |
| 2021 | Brandon Fernandes        | Margao             | GOA               |
| 2021 | Mandar Rao Dessai        | Mapusa             | GOA               |
| 2021 | Adil Khan                | Verna              | GOA               |
| 2021 | Mashoor Shereef          | Malappuram         | KERALA            |
| 2021 | Jeakson Singh Thounaojam | Thoubal            | MANIPUR           |
| 2021 | Rowllin Borges           | Nuvem              | GOA               |
| 2021 | Sahal Abdul Samad        | Payyanur           | KERALA            |
| 2021 | Raynier Fernandes        | Mumbai             | MAHARASHTRA       |
| 2021 | Pronay Halder            | Barrackpore        | WEST BENGAL       |
| 2021 | Hitesh Sharma            | Jalandhar          | PUNJAB            |
| 2021 | Manvir Singh             | Duhre              | PUNJAB            |
| 2021 | Sunil Chhetri            | Secunderabad       | TELANGANA         |
| 2021 | Liston Colaco            | Davorlim           | GOA               |
| 2021 | Bipin Singh              | Manipur            | MANIPUR           |
| 2021 | Udanta Singh             | Manipur            | MANIPUR           |
| 2021 | Ashique Kuruniyan        | Malappuram         | KERALA            |
| 2021 | Rahim Ali                | Barrackpore        | WEST BENGAL       |
| 2021 | Lallianzuala Chhangte    | Mizoram            | MIZORAM           |
| 2021 | Farukh Choudhary         | Ambarnath          | MAHARASHTRA       |
| 2021 | Ishan Pandita            | New Delhi          | DELHI             |
| 2021 | Holicharan Narzary       | Kokrajhar          | ASSAM             |
| 2022 | Gurpreet Singh Sandhu    | Chamkaur           | PUNJAB            |
| 2022 | Anwar Ali                | Adampur            | PUNJAB            |
| 2022 | Sandesh Jhingan          | Chandigarh         | CHANDIGARH        |
| 2022 | Akash Mishra             | Balrampur          | UTTAR PRADESH     |
| 2022 | Naorem Roshan Singh      | Samurou            | MANIPUR           |
| 2022 | Pritam Kotal             | Uttarpara          | WEST BENGAL       |
| 2022 | Subhasish Bose           | Kolkata            | WEST BENGAL       |
| 2022 | Chinglensana Singh       | Manipur            | MANIPUR           |
| 2022 | Rahul Bheke              | Mumbai             | MAHARASHTRA       |
| 2022 | Seriton Fernandes        | Goa                | GOA               |
| 2022 | Narender Gahlot          | Delhi              | "DELHI            |   |  " |
| 2022 | Hormipam Ruivah          | Somdal             | MANIPUR           |
| 2022 | Anirudh Thapa            | Dehradun           | HIMACHAL PRADESH  |
| 2022 | Sahal Abdul Samad        | Payyanur           | KERALA            |
| 2022 | Jeakson Singh Thounaojam | Thoubal            | MANIPUR           |
| 2022 | Suresh Singh Wangjam     | Manipur            | MANIPUR           |
| 2022 | Brandon Fernandes        | Margao             | GOA               |
| 2022 | Glan Martins             | Goa                | GOA               |
| 2022 | Danish Farooq            | Srinagar           | JAMMU AND KASHMIR |
| 2022 | Pronay Halder            | Barrackpore        | WEST BENGAL       |
| 2022 | Harmanjot Khabra         | Garhshankar        | PUNJAB            |
| 2022 | Sunil Chhetri            | Secunderabad       | TELANGANA         |
| 2022 | Manvir Singh             | Duhre              | PUNJAB            |
| 2022 | Ashique Kuruniyan        | Malappuram         | KERALA            |
| 2022 | Liston Colaco            | Davorlim           | GOA               |
| 2022 | Udanta Singh             | Manipur            | MANIPUR           |
| 2022 | Suhair Vadakkepeedika    | Mannarkkad         | KERALA            |
| 2022 | Rahim Ali                | Barrackpore        | WEST BENGAL       |
| 2022 | Ishan Pandita            | New Delhi          | "DELHI            |   |  " |
| 2022 | Lallianzuala Chhangte    | Mizoram            | MIZORAM           |
| 2022 | Aniket Jadhav            | Kolhapur           | MAHARASHTRA       |
| 2022 | Rahul Praveen            | Mannuthy           | KERALA            |
| 2023 | Gurpreet Singh Sandhu    | Chamkaur           | PUNJAB            |
| 2023 | Amrinder Singh           | Manolian           | PUNJAB            |
| 2023 | Akash Mishra             | Balrampur          | UTTAR PRADESH     |
| 2023 | Sandesh Jhingan          | Chandigarh         | CHANDIGARH        |
| 2023 | Anwar Ali                | Adampur            | PUNJAB            |
| 2023 | Mehtab Singh             | Khemkaran          | PUNJAB            |
| 2023 | Pritam Kotal             | Uttarpara          | WEST BENGAL       |
| 2023 | Subhasish Bose           | Kolkata            | WEST BENGAL       |
| 2023 | Rahul Bheke              | Mumbai             | MAHARASHTRA       |
| 2023 | Naorem Roshan Singh      | Samurou            | MANIPUR           |
| 2023 | Chinglensana Singh       | Manipur            | MANIPUR           |
| 2023 | Anirudh Thapa            | Dehradun           | HIMACHAL PRADESH  |
| 2023 | Jeakson Singh Thounaojam | Thoubal            | MANIPUR           |
| 2023 | Sahal Abdul Samad        | Payyanur           | KERALA            |
| 2023 | Nikhil Poojari           | Maharashtra        | MAHARASHTRA       |
| 2023 | Rohit Kumar              | New Delhi          | "DELHI            |   |  " |
| 2023 | Suresh Singh Wangjam     | Manipur            | MANIPUR           |
| 2023 | Brandon Fernandes        | Margao             | GOA               |
| 2023 | Rowllin Borges           | Nuvem              | GOA               |
| 2023 | Lalengmawia Ralte        | Aizawl             | MIZORAM           |
| 2023 | Ritwik Das               | Burnpur            | WEST BENGAL       |
| 2023 | Sunil Chhetri            | Secunderabad       | TELANGANA         |
| 2023 | Lallianzuala Chhangte    | Mizoram            | MIZORAM           |
| 2023 | Ashique Kuruniyan        | Malappuram         | KERALA            |
| 2023 | Naorem Mahesh Singh      | Manipur            | MANIPUR           |
| 2023 | Udanta Singh             | Manipur            | MANIPUR           |
| 2023 | Liston Colaco            | Davorlim           | GOA               |
| 2023 | Nandhakumar Sekar        | Chennai            | TAMIL NADU        |
| 2023 | Manvir Singh             | Duhre              | PUNJAB            |
| 2023 | Bipin Singh              | Manipur            | MANIPUR           |
| 2023 | Rahim Ali                | Barrackpore        | WEST BENGAL       |
| 2023 | Rahul Praveen            | Mannuthy           | KERALA            |
