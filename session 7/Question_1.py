import collections
import string


def analyse_text(text: str):
    hameye_kalamat = text.split()
    tedad_hameye_kalamat = len(hameye_kalamat)
    matne_bedoone_space = text.replace(' ', '')
    tedad_horoof = 0
    tedad_adad = 0
    bishtarin_bar_tekrar_harf = (matne_bedoone_space)
    bishtarin_bar_tekrar_kalame = (hameye_kalamat)
    for i in matne_bedoone_space:
        if not i.isdigit():
            tedad_horoof += 1
        if i.isdigit():
            tedad_adad += 1
    kalamat_bozorg = 0
    kalamat_koochak = 0
    for i in text:
        if i.isupper():
            kalamat_bozorg += 1
        if i.islower():
            kalamat_koochak += 1
    print("tedad e kalamate bozorg : ", kalamat_bozorg)
    print("tedad e kalamate kochak : ", kalamat_koochak)
    print("tedad e hameye kalamat: ", tedad_hameye_kalamat)
    print("tedad e adad: ", tedad_adad)
    print("tedad e horoof : ", tedad_horoof)
    print("bishtarin bar e tekrar e yek harf: ", bishtarin_bar_tekrar_harf)
    print("bishtarin bar e tekrar e yek kalame: ", bishtarin_bar_tekrar_kalame)



analyse_text("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore id aliquet lectus proin. Sapien faucibus et molestie ac feugiat sed lectus vestibulum. Ullamcorper velit sed ullamcorper morbi tincidunt ornare massa eget. Dictum varius duis at consectetur lorem. Nisi vitae suscipit tellus mauris a diam maecenas sed enim. Velit ut tortor pretium viverra suspendisse potenti nullam. Et molestie ac feugiat sed lectus. Non nisi est sit amet facilisis magna. Dignissim diam quis enim lobortis scelerisque fermentum. Odio ut enim blandit volutpat maecenas volutpat. Ornare lectus sit amet est placerat in egestas erat. Nisi vitae suscipit tellus mauris a diam maecenas sed. Placerat duis ultricies lacus sed turpis tincidunt id aliquet.")
