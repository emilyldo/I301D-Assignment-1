# I301D-Assignment-1
In the project, I analyzed data on the U.S. citizen voting-age population and voting rate from 2018.
I collected data on the 2018 U.S. citizen voting-age populations by U.S. congressional districts of every U.S. state, including population estimate, voting rate estimate, percentage of Bachelor's degree or more holding citizens, and percentage of below poverty level citizens.

This data comes from the U.S. Census Bureau website, specifically their datasets on "Number of Votes Cast, Citizen Voting-Age Population and Voting Rates for Congressional Districts: 2018", "Characteristics (Educational Attainment) of the Citizen Voting Age Population for Congressional Districts: 2018", and "Characteristics (Sex and Poverty) of the Citizen Voting-Age Population for Congressional Districts: 2018".

The following congressional districts were missing voting rate estimate data, and thus were removed from the dataset. 
Florida 10, Florida 14, Florida 21, Florida 24, North Carolina 9

The citizen voting-age populations were also converted into decimals for float formatting.
 
# Data Dictionary
state_name <class 'str'> Name of state
cong_district <class 'str'> Number of congressional district
voting_age_pop <class 'numpy.float64'> Citizen voting-age population estimate
voting_rate <class 'numpy.float64'> Voting rate estimate
bachelors_more_pct <class 'numpy.float64'> Bachelor's degree or more holding citizens percentage of total citizen voting-age population estimate
below_poverty_pct <class 'numpy.float64'> Below povery level citizens percentage of total citizen voting-age population estimate

# Analysis
I checked the frequency distribution of the voting rate, percentages of Bachelor's degrees or more holding citizens, and percentages of below poverty level citizens per congressional district, before comparing the voting rate to the latter two respectively. By doing so, I hoped to examine the extent of importance of these two demographical attributes for the 2018 U.S. voting rate. This analysis served to reveal any possible relationships between the 2018 U.S. voting rate and educational attainment or poverty status. 

# LICENSE
Copyright <YEAR> <COPYRIGHT HOLDER>
Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
