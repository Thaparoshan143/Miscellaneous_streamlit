import streamlit as st

st.title("Number Conversion")

col1, col2 = st.columns(2)

def reset():
    try:
        st.session_state.hex = '0'
        st.session_state.dec = '0'
        st.session_state.oct = '0'
        st.session_state.bin = '0'
    except:
        pass

def update_hex():
    try:
        if st.session_state.hex:
            st.success("Converted")
            hex_val = st.session_state.hex
            st.session_state.dec = repr(int("0x" + hex_val, 16))
            st.session_state.oct = oct(int("0x" + hex_val, 16))[2:]
            st.session_state.bin = bin(int("0x" + hex_val, 16))[2:]
    except:
        st.error("Invalid input")
        reset()

def update_dec():
    try:
        if st.session_state.dec:
            st.success("Converted")
            dec_val = st.session_state.dec
            st.session_state.hex = hex(int(dec_val, base=10))[2:]
            st.session_state.oct = oct(int(dec_val, base=10))[2:]
            st.session_state.bin = bin(int(dec_val, base=10))[2:]
    except:
        st.error("Invalid input")
        reset()

def update_oct():
    try:
        if st.session_state.oct:
            st.success("Converted")
            oct_val = st.session_state.oct
            st.session_state.hex = hex(int("0o" + oct_val, 8))[2:]
            st.session_state.dec = repr(int("0o" + oct_val, 8))
            st.session_state.bin = bin(int("0o" + oct_val, 8))[2:]
    except:
        st.error("Invalid input")
        reset()

def update_bin():
    try:
        if st.session_state.bin:
            st.success("Converted")
            bin_val = st.session_state.bin
            st.session_state.hex = hex(int("0b" + bin_val, 2))[2:]
            st.session_state.dec = repr(int("0b" + bin_val, 2))
            st.session_state.oct = oct(int("0b" + bin_val, 2))[2:]
    except:
        st.error("Invalid input")
        reset()


hexadecimal_input = col1.text_input("Hexdecimal", on_change=update_hex, key="hex")
decimal_input = col1.text_input("Decimal", on_change=update_dec, key="dec")
octal_input = col2.text_input("Octal", on_change=update_oct, key="oct")
binary_input = col2.text_input("Binary", on_change=update_bin, key="bin")
