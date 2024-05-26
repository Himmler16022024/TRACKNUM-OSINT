import os
import phonenumbers
from phonenumbers import carrier, geocoder, timezone
import platform

Bl = '\033[30m'
Re = '\033[1;31m'
Gr = '\033[1;32m'
Ye = '\033[1;33m'
Blu = '\033[1;34m'
Mage = '\033[1;35m'
Cy = '\033[1;36m'
Wh = '\033[1;37m'


def clear_screen():
    """Efface l'écran en fonction du système d'exploitation."""
    os_name = platform.system().lower()
    if os_name == 'windows':
        os.system('cls')
    else:
        os.system('clear')


def display_banner():
    """Affiche une bannière personnalisée."""
    clear_screen()
    print(f"""{Mage}
                                                                                                          
@@@**@@**@@@*@@@***@@m        @@        mm@***@m@*@@@@* *@@@*   *@@@m   *@@@**@@@*   *@@@**@@@@m     m@@@*
@*   @@   *@  @@   *@@m      m@@m     m@@*     *@  @@   m@*       @@@m    @   @@       @    @@@@    @@@@  
     @@       @@   m@@      m@*@@!    @@*       *  @@ m@*         @ @@@   @   @@       @    @ @@   m@ @@  
     !@       !@@@@@@      m@  *@@    @@           @@@@@m         @  *@@m @   @@       @    @  @!  @* @@  
     !@       !@  @@m      @@@!@!@@   @!m          !@  @@!        @   *@@m!   @@       !    !  @!m@*  @@  
     !@       !@   *!@    !*      @@  *!@m     m*  !@   *!!m      !     !@!   @@       !    !  *!@*   @@  
     !@       !@  ! !!     !!!!@!!@   !!!          !!    !:!      !   *!!!!   !@       !    !  !!!!*  !!  
     !!       !!   *!!!   !*      !!  :!!:     !*  !!     :!!!    !     !!!   !!!     !!    :  *!!*   !!  
   : :!::   : :!:  : : :: : :   : :::   : : : :! : : :      : : : : :    :!!   : : : :!:  : ::: :   : ::: 

                                                                                                        discord.gg/searchhub
                  
                                        {Wh}  C O D E   B Y   H I M M L E R  
        
    {Wh}[ 1 ] {Mage}TRACKNUM
    {Wh}[ 0 ] {Mage}Exit
""")


def phone_tracker():
    """Traque les informations d'un numéro de téléphone."""
    User_phone = input(f"\n {Wh}Entrer le numero {Mage}Ex [+963...] {Wh}: {Mage}")
    default_region = "ID"

    parsed_number = phonenumbers.parse(User_phone, default_region)
    region_code = phonenumbers.region_code_for_number(parsed_number)
    jenis_provider = carrier.name_for_number(parsed_number, "en")
    location = geocoder.description_for_number(parsed_number, "id")
    is_valid_number = phonenumbers.is_valid_number(parsed_number)
    is_possible_number = phonenumbers.is_possible_number(parsed_number)
    formatted_number = phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
    formatted_number_for_mobile = phonenumbers.format_number_for_mobile_dialing(parsed_number, default_region,
                                                                                 with_formatting=True)
    number_type = phonenumbers.number_type(parsed_number)
    timezone1 = timezone.time_zones_for_number(parsed_number)
    timezoneF = ', '.join(timezone1)

    print(f"\n {Wh}========== {Mage}INFORMATION DU NUMERO DE TELEPHONE {Wh}==========")
    print(f"\n {Wh}Location             :{Mage} {location}")
    print(f" {Wh}Region Code          :{Mage} {region_code}")
    print(f" {Wh}Timezone             :{Mage} {timezoneF}")
    print(f" {Wh}Operator             :{Mage} {jenis_provider}")
    print(f" {Wh}Valid number         :{Mage} {is_valid_number}")
    print(f" {Wh}Possible number      :{Mage} {is_possible_number}")
    print(f" {Wh}International format :{Mage} {formatted_number}")
    print(f" {Wh}Mobile format        :{Mage} {formatted_number_for_mobile}")
    print(f" {Wh}Original number      :{Mage} {parsed_number.national_number}")
    print(f" {Wh}E.164 format         :{Mage} {phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.E164)}")
    print(f" {Wh}Country code         :{Mage} {parsed_number.country_code}")
    print(f" {Wh}Local number         :{Mage} {parsed_number.national_number}")
    if number_type == phonenumbers.PhoneNumberType.MOBILE:
        print(f" {Wh}Type                 :{Mage} This is a mobile number")
    elif number_type == phonenumbers.PhoneNumberType.FIXED_LINE:
        print(f" {Wh}Type                 :{Mage} This is a fixed-line number")
    else:
        print(f" {Wh}Type                 :{Mage} This is another type of number")


def main_menu():
    """Affiche le menu principal et gère les choix de l'utilisateur."""
    while True:
        display_banner()
        input_user = input(f'\n   {Wh}Himmler~# {Mage}')

        if input_user == '1':
            phone_tracker()
            input(f"\nPress Enter to continue...")

        elif input_user == '0':
            print(f"\n  {Wh}[{Ye}!{Wh}] {Ye}Merci d'avoir utiliser le TOOL {Ye}TRACKNUM !")
            break

        else:
            print(f" {Ye}Ajoute une OPTION !") 


if __name__ == '__main__':
    main_menu()
