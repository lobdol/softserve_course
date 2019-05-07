def reverse(st):
    tmp_list=st.split(" ")
    tmp_list=tmp_list[-1::-1]
    st=" ".join(tmp_list)
    return st