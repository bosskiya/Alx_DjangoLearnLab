from graphviz import Digraph

# Create a new directed graph
erd = Digraph('ERD', filename='criminal_identification_erd', format='png')
erd.attr(rankdir='LR', size='10')

# Define entities
erd.node('Criminal', '''<<TABLE BORDER="1" CELLBORDER="1" CELLSPACING="0">
<TR><TD COLSPAN="2"><B>Criminal</B></TD></TR>
<TR><TD>IDNumber (PK)</TD><TD>Char(15)</TD></TR>
<TR><TD>FirstName</TD><TD>Char(20)</TD></TR>
<TR><TD>MiddleName</TD><TD>Char(20)</TD></TR>
<TR><TD>LastName</TD><TD>Char(20)</TD></TR>
<TR><TD>HolderDetective</TD><TD>FK to Detective</TD></TR>
<TR><TD>DOB</TD><TD>Date</TD></TR>
<TR><TD>Age</TD><TD>Int</TD></TR>
<TR><TD>Gender</TD><TD>Char(6)</TD></TR>
<TR><TD>Nationality</TD><TD>Char</TD></TR>
<TR><TD>Region</TD><TD>Char</TD></TR>
<TR><TD>Zone</TD><TD>Char</TD></TR>
<TR><TD>Woreda</TD><TD>Char</TD></TR>
<TR><TD>EducationLevel</TD><TD>Char</TD></TR>
<TR><TD>CrimeType</TD><TD>Char</TD></TR>
<TR><TD>Religion</TD><TD>Char</TD></TR>
<TR><TD>Status</TD><TD>Char</TD></TR>
<TR><TD>Image</TD><TD>Image</TD></TR>
</TABLE>>''')

erd.node('Detective', '''<<TABLE BORDER="1" CELLBORDER="1" CELLSPACING="0">
<TR><TD COLSPAN="2"><B>Detective</B></TD></TR>
<TR><TD>IDNumber (PK)</TD><TD>Char(15)</TD></TR>
<TR><TD>FirstName</TD><TD>Char(20)</TD></TR>
<TR><TD>MiddleName</TD><TD>Char(20)</TD></TR>
<TR><TD>LastName</TD><TD>Char(20)</TD></TR>
<TR><TD>DOB</TD><TD>Date</TD></TR>
<TR><TD>Age</TD><TD>Int</TD></TR>
<TR><TD>Gender</TD><TD>Char(6)</TD></TR>
<TR><TD>Region</TD><TD>Char(25)</TD></TR>
<TR><TD>Zone</TD><TD>Char(25)</TD></TR>
<TR><TD>Woreda</TD><TD>Char(25)</TD></TR>
<TR><TD>Role</TD><TD>Char(30)</TD></TR>
<TR><TD>Image</TD><TD>Image</TD></TR>
</TABLE>>''')

erd.node('Message', '''<<TABLE BORDER="1" CELLBORDER="1" CELLSPACING="0">
<TR><TD COLSPAN="2"><B>Message</B></TD></TR>
<TR><TD>MessageNum (PK)</TD><TD>Auto</TD></TR>
<TR><TD>Title</TD><TD>Char(30)</TD></TR>
<TR><TD>Sender</TD><TD>FK to Detective</TD></TR>
<TR><TD>Receiver</TD><TD>FK to Detective</TD></TR>
<TR><TD>Date</TD><TD>DateTime</TD></TR>
<TR><TD>Message</TD><TD>Text</TD></TR>
</TABLE>>''')

erd.node('Case', '''<<TABLE BORDER="1" CELLBORDER="1" CELLSPACING="0">
<TR><TD COLSPAN="2"><B>Case</B></TD></TR>
<TR><TD>ID_Number (PK)</TD><TD>Auto</TD></TR>
<TR><TD>CaseName</TD><TD>Char(100)</TD></TR>
<TR><TD>CaseType</TD><TD>Char(30)</TD></TR>
<TR><TD>AttackedBy</TD><TD>FK to Criminal</TD></TR>
<TR><TD>AttackedTo</TD><TD>FK to Criminal</TD></TR>
<TR><TD>AddedDate</TD><TD>DateTime</TD></TR>
</TABLE>>''')

# Define relationships
erd.edge('Criminal', 'Detective', label='HolderDetective')
erd.edge('Message', 'Detective', label='Sender')
erd.edge('Message', 'Detective', label='Receiver')
erd.edge('Case', 'Criminal', label='AttackedBy')
erd.edge('Case', 'Criminal', label='AttackedTo')

# Render ERD
erd.render(cleanup=True)
print("ERD saved as 'criminal_identification_erd.png'")
