# Email slicer in python programmming language

email_add = input("Enter a email: ")


def email(email_add="not given"):
    
    try: 
        at_count = email_add.count("@")
        at_index = email_add.index("@")
        p_count = email_add.count(".")
        characater_count = len(email_add)
        pt_after_at_count = email_add.count(".", at_index, len(email_add) + 1)
    except: 
        print("ERROR: An error occurred")
        quit()

    def error_handling(at_count, at_index, p_count, characater_count, pt_after_at_count):
        n = 0
        error_msg = []
        if(email_add == "not given" or email_add == ""):
             n = n + 1
             error_msg.append("Email not given")
        if(at_count > 1 ) or (at_index == 0) or (pt_after_at_count == 0): 
            n = n + 1
            error_msg.append("Invalid Email")
        if(characater_count > 64):
            n = n + 1
            error_msg.append("Email too long")
    
        if( n > 1 ):
            error_len = len(error_msg)
            for error in error_msg:
                print("ERROR!")
                print("     ", error)
            return 1
    error_h = error_handling(at_count, at_index, p_count, characater_count, pt_after_at_count)
    if(error_h == 1 ):
        quit()

    def slicer(at_index, email_add): 
        name = email_add[0:at_index]
        domain = email_add[at_index + 1: len(email_add)]
        print("user_name:", name)
        print("domain:", domain)
        return 0 

    slicer(at_index, email_add)
    return 0

email(email_add)