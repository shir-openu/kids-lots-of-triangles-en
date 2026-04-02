#!/usr/bin/env python3
"""Final pass - fix remaining Hebrew in page5_q6bcdef and page6."""
import os

BASE = os.path.dirname(os.path.abspath(__file__))

def read_file(name):
    with open(os.path.join(BASE, name), 'r', encoding='utf-8') as f:
        return f.read()

def write_file(name, content):
    with open(os.path.join(BASE, name), 'w', encoding='utf-8') as f:
        f.write(content)

def r(c, old, new):
    return c.replace(old, new)

# ============================================================
# page5_q6bcdef_analysis.html - remaining Hebrew
# ============================================================
c = read_file('page5_q6bcdef_analysis.html')

c = r(c, 'שאלה 6 - ניתוח מרחק מחיפה', 'Question 6 - Distance from Haifa Analysis')
c = r(c, 'שאלה 6 - משאית מחיפה', 'Question 6 - Truck from Haifa')
c = r(c, 'ניתוח גרף מרחק-זמן', 'Distance-Time Graph Analysis')
c = r(c, '<strong>משאית יצאה מחיפה. במהלך הנסיעה עצרה פעמיים.</strong>', '<strong>A truck left Haifa. During the trip it stopped twice.</strong>')
c = r(c, 'הגרף שלפניכם מתאר את המרחק מחיפה בהתאם לזמן שעבר מתחילת הנסיעה.', 'The graph below describes the distance from Haifa as a function of time elapsed since the start of the trip.')
c = r(c, '<h3>הגרף</h3>', '<h3>The Graph</h3>')
c = r(c, 'alt="גרף מרחק מחיפה"', 'alt="Distance from Haifa graph"')
c = r(c, '<h3>הטבלה</h3>', '<h3>The Table</h3>')
c = r(c, 'alt="טבלת ערכים"', 'alt="Value table"')
c = r(c, '<!-- שאלה ב -->', '<!-- Question B -->')
c = r(c, 'ב. באילו פרקי זמן לא נסעה המשאית? הסבירו.', 'B. During which time periods was the truck not moving? Explain.')
c = r(c, 'בחרו את התשובה הנכונה:', 'Choose the correct answer:')
c = r(c, 'בין שעה 0 ל-1 ובין שעה 4 ל-5', 'Between hour 0 and 1, and between hour 4 and 5')
c = r(c, 'בין שעה 1 ל-2 ובין שעה 3 ל-3.5 (כי הגרף אופקי - המרחק לא משתנה)', 'Between hour 1 and 2, and between hour 3 and 3.5 (graph is horizontal - distance unchanged)')
c = r(c, 'בין שעה 5 ל-7 (כי הגרף יורד)', 'Between hour 5 and 7 (graph descends)')
c = r(c, 'המשאית נסעה כל הזמן ללא הפסקה', 'The truck traveled continuously without stopping')
c = r(c, '>בדוק תשובה<', '>Check Answer<')
c = r(c, '<!-- שאלה ג -->', '<!-- Question C -->')
c = r(c, 'ג. האם חזרה המשאית לחיפה? הסבירו.', 'C. Did the truck return to Haifa? Explain.')
c = r(c, 'כן, המשאית חזרה לחיפה כי בזמן x=7 המרחק הוא y=0', 'Yes, the truck returned to Haifa because at time x=7 the distance is y=0')
c = r(c, 'לא, המשאית לא חזרה כי בסוף היא נשארה במרחק 100 ק"מ', 'No, the truck did not return because at the end it remained 100 km away')
c = r(c, 'לא ניתן לדעת מהגרף', 'Cannot be determined from the graph')
c = r(c, 'כן, כי היא עצרה פעמיים בדרך', 'Yes, because it stopped twice on the way')
c = r(c, '<!-- שאלה ד -->', '<!-- Question D -->')
c = r(c, 'ד. מה היה המרחק המרבי שלה מחיפה במהלך הנסיעה?', 'D. What was the maximum distance from Haifa during the trip?')
c = r(c, '100 ק"מ', '100 km')
c = r(c, '150 ק"מ', '150 km')
c = r(c, '200 ק"מ', '200 km')
c = r(c, '250 ק"מ', '250 km')
c = r(c, '<!-- שאלה ה -->', '<!-- Question E -->')
c = r(c, 'ה. האם ייתכן שבשני זמנים שונים היה אותו מרחק מחיפה?', 'E. Is it possible that at two different times the distance from Haifa was the same?')
c = r(c, 'כן, כי בדרך הלוך ובדרך חזור עברה המשאית באותם מרחקים', 'Yes, on the way out and back the truck passed through the same distances')
c = r(c, 'לא, לכל זמן יש מרחק שונה', 'No, each time has a different distance')
c = r(c, 'לא, כי זו פונקציה', 'No, because it is a function')
c = r(c, 'רק בזמן העצירות', 'Only during stops')
c = r(c, '<!-- שאלה ו -->', '<!-- Question F -->')
c = r(c, 'ו. האם y (המרחק) הוא פונקציה חד-חד-ערכית של x (הזמן)?', 'F. Is y (distance) a one-to-one function of x (time)?')
c = r(c, 'כן, כי לכל זמן מתאים מרחק יחיד', 'Yes, because each time corresponds to a unique distance')
c = r(c, 'לא, כי יש מרחקים שמתאימים ליותר מזמן אחד (למשל 150 ק"מ בהלוך ובחזור)', 'No, because some distances correspond to more than one time (e.g. 150 km on the way out and back)')
c = r(c, 'כן, כי הגרף עולה ויורד', 'Yes, because the graph rises and falls')
c = r(c, 'לא ניתן לקבוע', 'Cannot be determined')
c = r(c, '<strong>תזכורת:</strong> פונקציה <span class="highlight">חד-חד-ערכית</span> היא פונקציה שבה לכל Value y מתאים לכל היותר Value x אחד.', '<strong>Reminder:</strong> A <span class="highlight">one-to-one</span> function is one where each y value corresponds to at most one x value.')
c = r(c, 'במילים אחרות: כל קו אופקי חותך את הגרף לכל היותר בנקודה אחת.', 'In other words: every horizontal line intersects the graph at most at one point.')
c = r(c, 'סיימת את כל השאלות!', 'You completed all questions!')

# JS comments
c = r(c, '// בין שעה 1-2 ו-3-3.5 (גרף אופקי)', '// Between hour 1-2 and 3-3.5 (horizontal graph)')
c = r(c, '// כן, חזרה לחיפה (y=0 ב-x=7)', '// Yes, returned to Haifa (y=0 at x=7)')
c = r(c, '// 200 ק"מ', '// 200 km')
c = r(c, '// כן, בהלוך ובחזור', '// Yes, on the way out and back')
c = r(c, '// לא, לא חד-חד-ערכית', '// No, not one-to-one')

# JS feedback strings
c = r(c, "correct: '\u2713 Correct! \u05db\u05d0\u05e9\u05e8 \u05d4\u05d2\u05e8\u05e3 \u05d0\u05d5\u05e4\u05e7\u05d9, \u05d4\u05de\u05e8\u05d7\u05e7 \u05de\u05d7\u05d9\u05e4\u05d4 \u05dc\u05d0 \u05de\u05e9\u05ea\u05e0\u05d4 - \u05db\u05dc\u05d5\u05de\u05e8 \u05d4\u05de\u05e9\u05d0\u05d9\u05ea \u05e2\u05d5\u05de\u05d3\u05ea \u05d1\u05de\u05e7\u05d5\u05dd. \u05d6\u05d4 \u05e7\u05d5\u05e8\u05d4 \u05d1\u05d9\u05df \u05e9\u05e2\u05d4 1 \u05dc-2 \u05d5\u05d1\u05d9\u05df \u05e9\u05e2\u05d4 3 \u05dc-3.5.',",
    "correct: 'Correct! When the graph is horizontal, the distance from Haifa does not change - the truck is stationary. This occurs between hour 1-2 and hour 3-3.5.',")
c = r(c, "wrong: '\u2717 Incorrect. \u05d7\u05e4\u05e9\u05d5 \u05d0\u05ea \u05d4\u05e7\u05d8\u05e2\u05d9\u05dd \u05e9\u05d1\u05d4\u05dd \u05d4\u05d2\u05e8\u05e3 \u05d0\u05d5\u05e4\u05e7\u05d9 (\u05e9\u05d8\u05d5\u05d7) - \u05e9\u05dd \u05d4\u05de\u05e9\u05d0\u05d9\u05ea \u05dc\u05d0 \u05e0\u05e2\u05d4 \u05db\u05d9 \u05d4\u05de\u05e8\u05d7\u05e7 \u05dc\u05d0 \u05de\u05e9\u05ea\u05e0\u05d4.'",
    "wrong: 'Incorrect. Look for segments where the graph is horizontal (flat) - there the truck is not moving because the distance does not change.'")
c = r(c, "correct: '\u2713 Correct! \u05d1\u05e1\u05d5\u05e3 \u05d4\u05e0\u05e1\u05d9\u05e2\u05d4 (\u05d1\u05d6\u05de\u05df x=7) \u05d4\u05d2\u05e8\u05e3 \u05de\u05d2\u05d9\u05e2 \u05dc\u05e0\u05e7\u05d5\u05d3\u05d4 y=0, \u05db\u05dc\u05d5\u05de\u05e8 \u05d4\u05de\u05e9\u05d0\u05d9\u05ea \u05d7\u05d6\u05e8\u05d4 \u05dc\u05d7\u05d9\u05e4\u05d4.',",
    "correct: 'Correct! At the end of the trip (at time x=7) the graph reaches y=0, meaning the truck returned to Haifa.',")
c = r(c, "wrong: '\u2717 Incorrect. \u05d1\u05d3\u05e7\u05d5 \u05d0\u05ea \u05d4\u05d2\u05e8\u05e3 \u05d1\u05e0\u05e7\u05d5\u05d3\u05d4 x=7 - \u05de\u05d4 Value \u05d4-y \u05e9\u05dd? \u05d4\u05d0\u05dd \u05d4\u05d5\u05d0 \u05e9\u05d5\u05d5\u05d4 \u05dc-0?'",
    "wrong: 'Incorrect. Check the graph at point x=7 - what is the y value there? Is it equal to 0?'")
c = r(c, "correct: '\u2713 Correct! \u05d4\u05e0\u05e7\u05d5\u05d3\u05d4 \u05d4\u05d2\u05d1\u05d5\u05d4\u05d4 \u05d1\u05d9\u05d5\u05ea\u05e8 \u05d1\u05d2\u05e8\u05e3 \u05d4\u05d9\u05d0 200 \u05e7\"\u05de, \u05d5\u05d6\u05d4 \u05d4\u05de\u05e8\u05d7\u05e7 \u05d4\u05de\u05e8\u05d1\u05d9 \u05e9\u05d4\u05de\u05e9\u05d0\u05d9\u05ea \u05d4\u05ea\u05e8\u05d7\u05e7\u05d4 \u05de\u05d7\u05d9\u05e4\u05d4.',",
    "correct: 'Correct! The highest point on the graph is 200 km, the maximum distance the truck traveled from Haifa.',")
c = r(c, "wrong: '\u2717 Incorrect. \u05d4\u05de\u05e8\u05d7\u05e7 \u05d4\u05de\u05e8\u05d1\u05d9 \u05d4\u05d5\u05d0 \u05d4\u05e0\u05e7\u05d5\u05d3\u05d4 \u05d4\u05d2\u05d1\u05d5\u05d4\u05d4 \u05d1\u05d9\u05d5\u05ea\u05e8 \u05d1\u05d2\u05e8\u05e3 (\u05d4\u05e4\u05e1\u05d2\u05d4).'",
    "wrong: 'Incorrect. The maximum distance is the highest point on the graph (the peak).'")
c = r(c, "correct: '\u2713 Correct! \u05db\u05e9\u05d4\u05de\u05e9\u05d0\u05d9\u05ea \u05e0\u05e1\u05e2\u05d4 \u05de\u05d7\u05d9\u05e4\u05d4 \u05d5\u05d4\u05ea\u05e8\u05d7\u05e7\u05d4, \u05d5\u05d0\u05d6 \u05d7\u05d6\u05e8\u05d4 - \u05d4\u05d9\u05d0 \u05e2\u05d1\u05e8\u05d4 \u05d1\u05d0\u05d5\u05ea\u05dd \u05de\u05e8\u05d7\u05e7\u05d9\u05dd \u05e4\u05e2\u05de\u05d9\u05d9\u05dd (\u05e4\u05e2\u05dd \u05d1\u05d4\u05dc\u05d5\u05da \u05d5\u05e4\u05e2\u05dd \u05d1\u05d7\u05d6\u05d5\u05e8).',",
    "correct: 'Correct! When the truck traveled from Haifa and then returned, it passed through the same distances twice (once going and once returning).',")
c = r(c, "wrong: '\u2717 Incorrect. \u05d7\u05e9\u05d1\u05d5: \u05db\u05e9\u05d4\u05de\u05e9\u05d0\u05d9\u05ea \u05e0\u05d5\u05e1\u05e2\u05ea \u05d4\u05dc\u05d5\u05da \u05d5\u05d7\u05d6\u05d5\u05e8, \u05d4\u05d0\u05dd \u05d4\u05d9\u05d0 \u05e2\u05d5\u05d1\u05e8\u05ea \u05d1\u05d0\u05d5\u05ea\u05dd \u05de\u05e7\u05d5\u05de\u05d5\u05ea \u05d9\u05d5\u05ea\u05e8 \u05de\u05e4\u05e2\u05dd \u05d0\u05d7\u05ea?'",
    "wrong: 'Incorrect. Think: when the truck travels back and forth, does it pass through the same locations more than once?'")
c = r(c, "correct: '\u2713 Correct! \u05d4\u05e4\u05d5\u05e0\u05e7\u05e6\u05d9\u05d4 \u05d0\u05d9\u05e0\u05d4 \u05d7\u05d3-\u05d7\u05d3-\u05e2\u05e8\u05db\u05d9\u05ea \u05db\u05d9 \u05d9\u05e9 \u05e2\u05e8\u05db\u05d9 \u05de\u05e8\u05d7\u05e7 (y) \u05e9\u05de\u05ea\u05d0\u05d9\u05de\u05d9\u05dd \u05dc\u05d9\u05d5\u05ea\u05e8 \u05de\u05d6\u05de\u05df \u05d0\u05d7\u05d3 (x). \u05dc\u05de\u05e9\u05dc, \u05e7\u05d5 \u05d0\u05d5\u05e4\u05e7\u05d9 \u05d1-y=150 \u05d7\u05d5\u05ea\u05da \u05d0\u05ea \u05d4\u05d2\u05e8\u05e3 \u05d1\u05e9\u05ea\u05d9 \u05e0\u05e7\u05d5\u05d3\u05d5\u05ea.',",
    "correct: 'Correct! The function is not one-to-one because there are distance values (y) that correspond to more than one time (x). For example, a horizontal line at y=150 intersects the graph at two points.',")
c = r(c, "wrong: '\u2717 Incorrect. \u05d1\u05e4\u05d5\u05e0\u05e7\u05e6\u05d9\u05d4 \u05d7\u05d3-\u05d7\u05d3-\u05e2\u05e8\u05db\u05d9\u05ea, \u05dc\u05db\u05dc Value y \u05de\u05ea\u05d0\u05d9\u05dd \u05dc\u05db\u05dc \u05d4\u05d9\u05d5\u05ea\u05e8 Value x \u05d0\u05d7\u05d3. \u05d4\u05d0\u05dd \u05d6\u05d4 \u05d4\u05de\u05e6\u05d1 \u05db\u05d0\u05df?'",
    "wrong: 'Incorrect. In a one-to-one function, each y value corresponds to at most one x value. Is that the case here?'")

c = r(c, "alert('\u05d0\u05e0\u05d0 \u05d1\u05d7\u05e8 \u05ea\u05e9\u05d5\u05d1\u05d4');", "alert('Please select an answer');")

c = r(c, '\u00a9 Developed by Shir Sivroni', '\u00a9 Developed by Shir Sivroni')

write_file('page5_q6bcdef_analysis.html', c)
print('page5_q6bcdef_analysis.html done')

# ============================================================
# page6.html
# ============================================================
c = read_file('page6.html')

c = r(c, 'Page 6 - \u05e9\u05d0\u05dc\u05d4 \u05de\u05e1\u05db\u05de\u05ea: \u05d4\u05e4\u05d5\u05e0\u05e7\u05e6\u05d9\u05d4 \u05d4\u05e7\u05d5\u05d5\u05d9\u05ea', 'Page 6 - Summary Question: The Linear Function')
c = r(c, '\u05e0\u05d9\u05e7\u05d5\u05d3', 'Score')
c = r(c, '\u05e9\u05d0\u05dc\u05d4 \u05de\u05e1\u05db\u05de\u05ea: \u05d4\u05e4\u05d5\u05e0\u05e7\u05e6\u05d9\u05d4 \u05d4\u05e7\u05d5\u05d5\u05d9\u05ea', 'Summary Question: The Linear Function')
c = r(c, '\u05d7\u05d5\u05e4\u05e9\u05ea \u05d7\u05e0\u05d5\u05db\u05d4 \u05ea\u05e9\u05e4"\u05d4', "Hanukkah Break 5785")

# Question comments and titles
c = r(c, '<!-- Question \u05d0 -->', '<!-- Question A -->')
c = r(c, '\u05d0. \u05de\u05e6\u05d0\u05d5 \u05d0\u05ea \u05d4\u05e4\u05d5\u05e0\u05e7\u05e6\u05d9\u05d4 f(x)', 'A. Find the function f(x)')
c = r(c, 'f(x) \u05e2\u05d5\u05d1\u05e8\u05ea \u05d3\u05e8\u05da \u05e8\u05d0\u05e9\u05d9\u05ea \u05d4\u05e6\u05d9\u05e8\u05d9\u05dd O(0,0).', 'f(x) passes through the origin O(0,0).')
c = r(c, '<!-- Question \u05d1 -->', '<!-- Question B -->')
c = r(c, '\u05d1. \u05de\u05e6\u05d0\u05d5 \u05d0\u05ea \u05e9\u05d9\u05e2\u05d5\u05e8 \u05d4-x \u05e9\u05dc \u05d4\u05e0\u05e7\u05d5\u05d3\u05d4 B', 'B. Find the x-coordinate of point B')
c = r(c, '\u05e0\u05ea\u05d5\u05df \u05e9\u05e9\u05d9\u05e2\u05d5\u05e8 \u05d4-y \u05e9\u05dc \u05d4\u05e0\u05e7\u05d5\u05d3\u05d4 B \u05d4\u05d5\u05d0 6. B \u05e0\u05de\u05e6\u05d0\u05ea \u05e2\u05dc g(x).', 'Given that the y-coordinate of point B is 6. B is on g(x).')
c = r(c, '<!-- Question \u05d2 -->', '<!-- Question C -->')
c = r(c, '\u05d2. \u05de\u05e6\u05d0\u05d5 \u05d0\u05ea \u05d4\u05e4\u05d5\u05e0\u05e7\u05e6\u05d9\u05d4 g(x)', 'C. Find the function g(x)')
c = r(c, 'g(x) \u05e2\u05d5\u05d1\u05e8\u05ea \u05d3\u05e8\u05da D(0,12) \u05d5-C(4,0).', 'g(x) passes through D(0,12) and C(4,0).')
c = r(c, '<!-- Question \u05d3 -->', '<!-- Question D -->')
c = r(c, '\u05d3. \u05de\u05e6\u05d0\u05d5 \u05d0\u05ea \u05e9\u05d9\u05e2\u05d5\u05e8\u05d9 \u05d4\u05e0\u05e7\u05d5\u05d3\u05d4 E', 'D. Find the coordinates of point E')
c = r(c, 'E \u05e0\u05de\u05e6\u05d0\u05ea \u05e2\u05dc f(x).', 'E is on f(x).')
c = r(c, '<!-- Question \u05d4 - True/False -->', '<!-- Question E - True/False -->')
c = r(c, '\u05d4. \u05d8\u05e2\u05e0\u05d5\u05ea \u05e0\u05db\u05d5\u05df/Incorrect', 'E. True/False Statements')
c = r(c, "1. \u05d0\u05d5\u05e8\u05da \u05d4\u05e7\u05d8\u05e2 DE \u05d4\u05d5\u05d0 10 \u05d9\u05d7'", '1. The length of segment DE is 10 units')
c = r(c, '>\u05e0\u05db\u05d5\u05df<', '>True<')
c = r(c, '2. \u05e9\u05d8\u05d7 \u05d4\u05de\u05e9\u05d5\u05dc\u05e9 \u25b3ABC \u05d4\u05d5\u05d0 30 \u05d9\u05d7"\u05e8', '2. Area of triangle \u25b3ABC is 30 sq. units')
c = r(c, '<!-- Question \u05d5 -->', '<!-- Question F -->')
c = r(c, '\u05d5. \u05de\u05e9\u05d5\u05d5\u05d0\u05d5\u05ea \u05d4\u05e7\u05d8\u05e2\u05d9\u05dd CE \u05d5-AD', 'F. Equations of segments CE and AD')
c = r(c, '1. \u05de\u05e9\u05d5\u05d5\u05d0\u05ea \u05d4\u05e7\u05d8\u05e2 CE:', '1. Equation of segment CE:')
c = r(c, '2. \u05de\u05e9\u05d5\u05d5\u05d0\u05ea \u05d4\u05e7\u05d8\u05e2 AD:', '2. Equation of segment AD:')
c = r(c, '<!-- Question \u05d6 -->', '<!-- Question G -->')
c = r(c, '\u05d6. \u05e1\u05d3\u05e8 \u05e9\u05d8\u05d7\u05d9 \u05d4\u05de\u05e9\u05d5\u05dc\u05e9\u05d9\u05dd \u05dc\u05e4\u05d9 \u05d2\u05d5\u05d3\u05dc\u05dd', 'G. Order triangle areas by size')
c = r(c, '\u05e1\u05d3\u05e8\u05d5 \u05d0\u05ea \u05d4\u05de\u05e9\u05d5\u05dc\u05e9\u05d9\u05dd \u0394CEO, \u0394BDE, \u05d5-\u0394ADE \u05de\u05d4\u05e7\u05d8\u05df \u05dc\u05d2\u05d3\u05d5\u05dc:', 'Order the triangles \u0394CEO, \u0394BDE, and \u0394ADE from smallest to largest:')
c = r(c, '\u05e9\u05d8\u05d7 CEO = 12 \u05d9\u05d7"\u05e8 | \u05e9\u05d8\u05d7 BDE = 24 \u05d9\u05d7"\u05e8 | \u05e9\u05d8\u05d7 ADE = 24 \u05d9\u05d7"\u05e8', 'Area CEO = 12 sq. units | Area BDE = 24 sq. units | Area ADE = 24 sq. units')
c = r(c, '<!-- Question \u05d7 -->', '<!-- Question H -->')
c = r(c, '\u05d7. \u05de\u05e9\u05d5\u05d5\u05d0\u05d5\u05ea \u05d9\u05e9\u05e8\u05d9\u05dd \u05e0\u05d5\u05e1\u05e4\u05d9\u05dd', 'H. Additional Line Equations')
c = r(c, '1. \u05de\u05e9\u05d5\u05d5\u05d0\u05ea \u05d4\u05d9\u05e9\u05e8 \u05d4\u05e2\u05d5\u05d1\u05e8 \u05d3\u05e8\u05da B \u05d5\u05de\u05e7\u05d1\u05d9\u05dc \u05dc\u05e6\u05d9\u05e8 \u05d4-x:', '1. Equation of the line through B parallel to the x-axis:')
c = r(c, '2. \u05de\u05e9\u05d5\u05d5\u05d0\u05ea \u05d4\u05d9\u05e9\u05e8 \u05d4\u05e2\u05d5\u05d1\u05e8 \u05d3\u05e8\u05da C \u05d5\u05de\u05e7\u05d1\u05d9\u05dc \u05dc\u05e6\u05d9\u05e8 \u05d4-y:', '2. Equation of the line through C parallel to the y-axis:')

# JS
c = r(c, "feedback.textContent = 'Correct! \u05ea\u05e9\u05d5\u05d1\u05d4 \u05de\u05e6\u05d5\u05d9\u05e0\u05ea!';", "feedback.textContent = 'Correct! Excellent answer!';")
c = r(c, "feedback.textContent = 'Incorrect. \u05d4\u05ea\u05e9\u05d5\u05d1\u05d4 \u05d4\u05e0\u05db\u05d5\u05e0\u05d4: ' + correctAnswers[q];", "feedback.textContent = 'Incorrect. The correct answer is: ' + correctAnswers[q];")
c = r(c, "const correctText = tfAnswers[q] ? '\u05e0\u05db\u05d5\u05df' : 'Incorrect';", "const correctText = tfAnswers[q] ? 'True' : 'False';")
c = r(c, "feedback.textContent = 'Incorrect. \u05d4\u05ea\u05e9\u05d5\u05d1\u05d4 \u05d4\u05e0\u05db\u05d5\u05e0\u05d4: ' + correctText;", "feedback.textContent = 'Incorrect. The correct answer is: ' + correctText;")
c = r(c, "feedback.textContent = 'Incorrect. \u05d4\u05ea\u05e9\u05d5\u05d1\u05d4 \u05d4\u05e0\u05db\u05d5\u05e0\u05d4: ' + segAnswers[q];", "feedback.textContent = 'Incorrect. The correct answer is: ' + segAnswers[q];")
c = r(c, "feedback.textContent = 'Incorrect. \u05d4\u05ea\u05e9\u05d5\u05d1\u05d4 \u05d4\u05e0\u05db\u05d5\u05e0\u05d4: ' + lineAnswers[q];", "feedback.textContent = 'Incorrect. The correct answer is: ' + lineAnswers[q];")

c = r(c, '\u00a9 Developed by Shir Sivroni', '\u00a9 Developed by Shir Sivroni')

write_file('page6.html', c)
print('page6.html done')

print('=== PASS 4 DONE ===')
