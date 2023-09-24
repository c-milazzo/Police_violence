import streamlit as st

st.title("Credits:")

url = 'https://www.washingtonpost.com/graphics/investigations/police-shootings-database/'

st.markdown(f'''<a href={url}><button style="background-color:GreenYellow
;">The Washington Post Police Shootings Database</button></a> ''', unsafe_allow_html=True)


st.text("""Research and reporting: Jennifer Jenkins, Monika Mathur, Razzan 
Nakhlawi, Steven Rich and Andrew Ba Tran.

Design and development: Chris Alcantara, Katlyn Alo, Emma Baker, 
Aaron Brezel, Armand Emamdjomeh, Jake Kara, Paige Moody, James O’Toole and 
Leslie Shapiro.

Editing: Sarah Childress, David Fallis, Reuben Fischer-Baum, Meghan Hoyer 
and Courtney Kan.

Past contributors: Keith L. Alexander, Sophie Andrews, Jason Bartz, 
Amy Brittain, Swetabh Changkakoti, Hong Sen Du, Kennedy Elliot, 
Linda Epstein, Holden Foreman, Joe Fox, Wendy Galietta, Kaeti Hinck, 
Laris Karklis, Kimberly Kindy, Whitney Leaming, Emily Liu, Wesley Lowery, 
Ted Mellnik, Lori Montgomery, Deblina Mukherjee, John Muyskens, Erik Reyna, 
Danielle Rindler, Kavya Sukumar, Julie Tate, Susan Tyler, Divya Verma, 
Aaron Williams. """ )
