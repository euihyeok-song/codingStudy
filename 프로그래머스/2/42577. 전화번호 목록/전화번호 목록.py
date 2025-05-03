def solution(phone_book):
    
    phone_book = sorted(phone_book)
    book_len = len(phone_book)
    
    for idx,val in enumerate(phone_book):
        
        if idx < book_len-1 and phone_book[idx+1].startswith(val):
            return False
    
    return True