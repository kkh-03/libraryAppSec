from db import get_cursor

def update_member():
    conn, cursor = get_cursor()
    
    try:
        student_seq = int(input("수정할 성적의 고유 ID(id_grade) 입력:" ))

        cursor.execute("SELECT subject, score FROM grades WHERE id_grade = %s", (student_seq,))
        rows = cursor.fetchone()

        if not rows:
            print("해당 학생이 없습니다.")
            return
        
        subject = rows[0]
        score = rows[1]

        print(f"--- 현재 정보 : {subject} ({score}점) ---")

        update_score = int(input("수정할 점수 입력: "))
        
        sql = "UPDATE grades SET score = %s WHERE id_grade = %s"
        cursor.execute(sql, (update_score, student_seq))
        conn.commit()

        print(f"[시스템] 성적 수정이 완료되었습니다. ({score}점 -> {update_score}점)")
        

    except Exception as e:
        print("수정 실패:", e)

    finally:
        cursor.close()
        conn.close()