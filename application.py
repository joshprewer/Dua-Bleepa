import streamlit as st
import gpt_2_simple as gpt2
import tensorflow as tf

def main():
    st.title("Dua Bleepa")

    sess = gpt2.start_tf_sess()

    data_load_state = st.text('Loading model...')
    gpt2.load_gpt2(sess, run_name='run1')
    data_load_state.text('')

    if st.button('Write me a song Dua'):
        data_load_state.text('Generating a song (this may take me a while tehe)...')
        text = gpt2.generate(sess,
                            prefix='<|startoftext|>',
                            truncate='<|endoftext|>',
                            include_prefix=False,
                            return_as_list=True
                            )[0]

        data_load_state.text('Generated song:')
        lyrics = st.text(text)

if __name__ == "__main__":
    main()