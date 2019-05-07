def correct_tail(body, tail):
     sub = len(body)
     print(sub) 
     body_tail=body[sub]
     print (body_tail)
         if body_tail == tail:
            return True
         else:
            return False

correct_tail("Fox", "x")
