# Definição de personagens
define m = Character("Mia", color="#FFC0CB")
define ex = Character("Ex", color="#FF0000")
define f = Character("Amiga", color="#00FF00")
define n = Character(None)


define music_rock = "illurock.opus"

#########################################
# INTRODUÇÃO
#########################################

label start:
    scene bg uni with fade
    play music music_rock
    n "Cicatrizes Invisíveis"
    n "Gênero: Drama Psicológico / Aventura Narrativa"
    n "Nesta história, você assume o papel de Mia, uma mulher que luta para reconstruir sua vida após um relacionamento tóxico e abusivo."
    
    menu:
        "Deseja revisitar as memórias do relacionamento?"
        "Sim, quero ver as memórias":
            jump flashback_menu
        "Não, seguir para o presente":
            jump presente

#########################################
# FLASHBACK – MEMÓRIAS DO PASSADO
#########################################

label flashback_menu:
    scene bg lecturehall with fade
    n "Reviver o passado pode ser doloroso, mas pode ajudar a compreender os abusos que marcaram sua história."
    menu:
        "Escolha a perspectiva para as memórias?"
        "Perspectiva de Mia":
            jump flashback_mia
        "Perspectiva do Ex":
            jump flashback_ex

label flashback_mia:
    scene bg club with dissolve
    show sylvie green normal
    m "Eu lembro claramente da primeira vez que ele entrou na minha vida..."
    jump flashback_conclude

label flashback_ex:
    scene bg club with dissolve
    show sylvie green surprised
    ex "Eu sempre acreditei que o que tínhamos era especial..."
    jump flashback_conclude

label flashback_conclude:
    n "Agora, é hora de voltar ao presente e enfrentar as cicatrizes invisíveis que ainda te acompanham."
    jump presente

#########################################
# PRESENTE – A JORNADA DE MIA
#########################################

label presente:
    scene bg meadow with fade
    show sylvie green smile
    n "Você retorna ao presente. Mia, determinada a se libertar do ciclo de abuso, inicia sua jornada de cura."
    jump ato1

label ato1:
    scene bg lecturehall with fade
    show sylvie green normal
    m "Mesmo após o fim, sinto que ele ainda está presente..."
    menu:
        "Seu celular vibra. O que você faz?"
        "Ignorar a mensagem":
            jump ato1_ignorar
        "Abrir a mensagem":
            jump ato1_abrir

label ato1_ignorar:
    show sylvie green surprised
    m "Fecho os olhos, tentando ignorar a mensagem..."
    jump ato1_continue

label ato1_abrir:
    show sylvie green normal
    m "Respiro fundo e deslizo o dedo para abrir a mensagem."
    jump ato1_continue

label ato1_continue:
    menu:
        "Como você reage neste momento de vulnerabilidade?"
        "Mergulhar na dor e reviver cada detalhe":
            jump ato1_detalhes
        "Procurar apoio para enfrentar essa escuridão":
            jump ato1_apoio

label ato1_detalhes:
    show sylvie green surprised
    m "Deixo-me levar pela dor, revivendo cada humilhação..."
    jump ato2

label ato1_apoio:
    show sylvie green smile
    f "Mia, sei o quanto essa dor é profunda. Mas você é muito mais do que tudo isso."
    jump ato2

label ato2:
    scene bg uni with fade
    show sylvie green smile
    n "ATO 2: Reconstrução"
    menu:
        "Durante esse processo, você decide:"
        "Enfrentar diretamente as lembranças dolorosas":
            jump ato2_enfrentar
        "Focar em construir novas experiências e memórias":
            jump ato2_novamemoria

label ato2_enfrentar:
    show sylvie green surprised
    m "Determino enfrentar cada lembrança..."
    jump ato3

label ato2_novamemoria:
    show sylvie green normal
    m "Decido que é hora de construir algo novo..."
    jump ato3

label ato3:
    scene bg meadow with fade
    show sylvie green normal
    n "ATO 3: Libertação ou Retorno"
    menu:
        "Escolha seu destino final:"
        "Final de Superação":
            jump final_superacao
        "Final de Enfrentamento":
            jump final_enfrentamento
        "Final de Recaída":
            jump final_recaida

label final_superacao:
    scene bg club with fade
    show sylvie green smile
    n "FINAL DE SUPERAÇÃO: Mia segue seu caminho..."
    jump fim

label final_enfrentamento:
    scene bg lecturehall with fade
    show sylvie green normal
    n "FINAL DE ENFRENTAMENTO: Mia confronta seu passado..."
    jump fim

label final_recaida:
    scene bg uni with fade
    show sylvie green surprised
    n "FINAL DE RECAÍDA: Mia retorna ao relacionamento abusivo..."
    jump fim

label fim:
    scene black with fade
    n "Obrigado por vivenciar 'Cicatrizes Invisíveis'."
    return
