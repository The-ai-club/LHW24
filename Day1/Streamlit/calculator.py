import streamlit as st 

a = st.number_input("Enter the first number:")
b = st.number_input("Enter the second number:")
operation = st.selectbox(label = "select your operation", 
                         options=["Addition", "subtraction",
                          "multiplication", "division"])


# cimage = st.camera_input("say cheese")
# if cimage:
#     st.image(cimage)
if st.button("Calculate"):
    if operation=='Addition':
        c = a+b
        st.header("The sum of a and b is: "+str(c))
    elif operation =='subtraction':
        c = a-b 
        st.header("The subtractoin of a and b is: "+str(c))
    elif operation =='multiplication':
        c=a*b 
        st.header("The multiplication of a and b is " + str(c))
    else: 
        if b==0:
            st.error("dont divide by zero")
        else:
            c = a/b 
            st.header("The division of a and b is" + str(c))