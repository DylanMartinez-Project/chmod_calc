import streamlit as st



st.header(":penguin: Chmod Calculator :penguin:")
st.subheader("This will help calculate the octal & symbolic representation of the Chmod liniux command for file permissions")
summary = "The `chmod` command is used to change the permissions of files and directories.\n\n" \
          "The permissions can be represented using both octal and symbolic values:\n\n" \
          "1. Octal Values:\n" \
          "\t- Each permission (read, write, execute) is assigned a numeric value: read (4), write (2), execute (1).\n" \
          "\t- These values are combined to represent the permissions for the owner, group, and others.\n" \
          "\t- For example, the octal value 755 represents the permissions: owner (read, write, execute), group (read, execute), others (read, execute).\n\n" \
          "2. Symbolic Values:\n" \
          "\t- The symbolic representation provides a more human-readable format.\n" \
          "\t- It uses letters and symbols to represent permissions.\n" \
          "\t- The permissions are divided into three sets: owner (u), group (g), others (o).\n" \
          "\t- The symbols used are: read (r), write (w), execute (x), and a hyphen (-) to indicate no permission.\n" \
          "\t- For example, the symbolic value `u=rwx,g=rx,o=rx` represents the same permissions as octal 755."
st.text(summary)
col1, col2, col3 = st.columns(3)

with col1:
   st.header("Owner")
   st.write('---')


   owner_octal=0
   readint = 0
   writeint =0
   executeint=0

   Read = st.checkbox('Read')
   if Read:
      readint= 4
   Write = st.checkbox('Write')
   if Write: 
      writeint=2 
   Execute = st.checkbox('Execute')
   if Execute:
      executeint=1

   owner_octal = readint + writeint + executeint
   st.write('---')


with col2:
   st.header("Group")
   st.write('---')
   group_octal =0
   readint2 = 0
   writeint2 =0
   executeint2=0


   Read2 = st.checkbox(' Read')
   if Read2:
      readint2= 4
   Write2 = st.checkbox(' Write')
   if Write2: 
      writeint2=2 
   Execute2 = st.checkbox(' Execute')
   if Execute2:
      executeint2=1

   group_octal =readint2 + writeint2 + executeint2
   st.write('---')


with col3:
   st.header("Public/Others")
   st.write('---')
   pub_octal = 0
   readint3 = 0
   writeint3 =0
   executeint3=0


   Read3 = st.checkbox('Read ')
   if Read3:
      readint3= 4
   Write3 = st.checkbox('Write ')
   if Write3: 
      writeint3=2 
   Execute3 = st.checkbox('Execute ')
   if Execute3:
      executeint3=1

   pub_octal =readint3 + writeint3 + executeint3
   st.write('---')


st.subheader(":paperclip: Linux Permissions calculated 	:paperclip:")
c1,c2= st.columns(2)

owner_octal = str(owner_octal)
group_octal = str(group_octal)
pub_octal = str (pub_octal) 
final_oct= owner_octal+group_octal+pub_octal

int_final_oct = int(final_oct)
#st.write(int_final_oct)




def octal_to_symbolic(octal):
    permissions = {
        0: r'---',
        1: r'--x',
        2: r'-w-',
        3: r'-wx',
        4: r'r--',
        5: r'r-x',
        6: r'rw-',
        7: r'rwx'
    }

    symbolic = ''
    for digit in str(octal):
        
        symbolic += permissions[int(digit)]

    return symbolic

symbolic_value= octal_to_symbolic(final_oct)
st.code(symbolic_value)




c1.metric(label="Octal Value", value=final_oct)
c2.metric(label="Symbolic Value", value=symbolic_value)







