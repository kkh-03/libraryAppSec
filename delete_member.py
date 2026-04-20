from db import get_cursor

def delete_member():
    conn, cursor = get_cursor()
    
    try:
        student_seq = int(input("삭제할 성적의 고유 ID(id_grade) 입력:" ))

        cursor.execute("SELECT seq, subject FROM student WHERE seq = %s", (student_seq,))
        rows = cursor.fetchone()

        if not rows:
            print("해당 학생이 없습니다.")
            return


        subject = rows[1]
        
        delete_message = str(input("정말로 삭제 하시겠습니까? (y/n): "))

        if delete_message == 'y':

            sql = """DELETE FROM student WHERE seq =  %s """
        
            cursor.execute(sql, (student_seq,))
            conn.commit()

            print(f"[시스템] {student_seq}번 성적 데이터가 삭제되었습니다. (대상: {subject})")

        else:
            print("삭제 취소됨")
        
    except Exception as e:
        print("삭제 실패:", e)

    finally:
        cursor.close()
        conn.close()