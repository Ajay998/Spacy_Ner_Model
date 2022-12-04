import spacy
from connect_database import mycursor,db
nlp=spacy.load("org_model8")
numbers=[0,1,2,3,4,5,6,7,8,9]
#
# case_id=364
# def find_ORG(case_id):
    # current_status = False
    # mycursor.execute(f"select current_status from case_process_status where case_id = {case_id}")
    # myresult = mycursor.fetchall()
    # for x in myresult:
    #     if x[0] == 3:
    #         current_status = True
    #         break
    #
    # if current_status == False:
    # pages=[]
    # correct_word = None
case_id = 372
mycursor.execute(f"select page_number,page_content from mt_page_file_contents where fk_case_id = {case_id}")
myresult = mycursor.fetchall()
for x in myresult:
        page_number=x[0]
        text=x[1]
        doc = nlp(text)
        for y in doc.ents:
            print(y,"pageno",page_number)
            for k in numbers:
                   if str(k) not in y.text:
                       correct_word = True
                   else:
                       correct_word = False
                       break
            if correct_word ==True and page_number not in pages:
                   pages.append(page_number)
                   mycursor.execute("INSERT INTO ai_org(case_id,page_number,org_name) VALUES (%s,%s,%s)",(case_id, page_number, y.text))
                   db.commit()
                   print(y.text)
    #
    #
    # mycursor.execute("INSERT INTO case_process_status(case_id,current_status)  VALUES (%s,%s)",(case_id, 3))
    # db.commit()
    # print(f"current status for case_id{case_id} is  3")

