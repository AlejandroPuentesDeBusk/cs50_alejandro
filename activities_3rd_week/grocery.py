


def add():

    dic = {

}
    new={

    }

    a = 0


    while True:

        try:

            items =str(input("").upper())



            if items in dic:

                dic[items] = dic[items] + 1

            else:
                  dic[items] = 1


        except EOFError:

            for clave in sorted(dic):

                new[clave] = dic[clave]


            for clave,valor in new.items():

                print(f"{valor} {clave}")

            break


add()
