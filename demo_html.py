import smtplib
from email.message import EmailMessage
import imghdr
from string import Template


def get_contacts(filename):
    names = []
    emails_to = []
    with open(filename, mode='r', encoding='utf-8') as contacts_file:
        for a_contact in contacts_file:
            names.append(a_contact.split()[0])
            emails_to.append(a_contact.split()[1])
    return names, emails_to


email_add = 'champion300102@gmail.com'
password_me = 'atikin123'

name, to = get_contacts('mycontacts.txt')
for i in range(len(to)):
    msg = EmailMessage()
    msg['Subject'] = 'PYTHON WORLD'
    msg['From'] = email_add
    msg['to'] = to[i]
    msg.set_content(f"Hello {name[i]}")
    msg.add_alternative("""\
    <!DOCTYPE html>
<h1>2. <strong>SQUID GAME</strong> Problem Code:</h1>
<p><strong>GAME INFO :-</strong></p>
<p>Sachin is planning to play a real SQUID GAME . The game is to collect maximum number of rings along a straight line of boxes. Each box has a certain amount of rings, the only constraint stopping Sachin from getting rings from each of the box &nbsp;is that adjacent boxes have security systems connected and <strong>it will automatically shoot him If the ring comes out from two adjacent boxes.</strong></p>
<p>Given an integer array nums representing the amount of rings of each box, return <em>the maximum amount of rings Sachin can get <strong>without alerting</strong></em>.</p>
<p><strong>Input</strong></p>
<p>The first line of the input contains an integer <strong>T</strong> denoting the number of test cases. The description of <strong>T</strong> test cases follows.</p>
<ul>
    <li>The first line of each test case contains <strong>n</strong> space-separated integers or elements of array</li>
</ul>
<p><strong>Output</strong></p>
<p>For each test case, output a single line containing the maximum number of rings Sachin get&rsquo;s</p>
<p><strong>Constraints</strong></p>
<ul>
    <li>1 &lt;= nums.length &lt;= 100</li>
    <li>0 &lt;= nums[i] &lt;= 400</li>
</ul>
<p><strong>Sample Input 1</strong></p>
<p>2</p>
<p>8 9 10 1</p>
<p>4 3 2 1 0 19</p>
<p><strong>Sample Output 1</strong></p>
<p>18</p>
<p>25</p>
<p><strong>Explanation</strong></p>
<p><strong>Example case 1.</strong> Get rings from box 1 (rings = 8) and then get rings from box 3 (rings = 10)</p>
        
        """, subtype="html")

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(email_add, password_me)
        smtp.send_message(msg)

