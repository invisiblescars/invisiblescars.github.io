# script.rpy

# Definição de personagens
define m = Character("Mia", color="#FFC0CB")
define ex = Character("Ex", color="#FF0000")
define f = Character("Amiga", color="#00FF00")
define n = Character(None)

#########################################
# INTRODUÇÃO
#########################################

label start:
    scene bg_title with fade
    n "Cicatrizes Invisíveis"
    n "Gênero: Drama Psicológico / Aventura Narrativa"
    n "Nesta história, você assume o papel de Mia, uma mulher que luta para reconstruir sua vida após um relacionamento tóxico e abusivo."
    n "Memórias dolorosas, mensagens enigmáticas e sombras do passado a assombram, enquanto uma presença – a personificação do seu ex – insiste em tentar trazê-la de volta ao ciclo do abuso."
    n "Você terá a oportunidade de revisitar essas memórias através de flashbacks, explorando a história sob duas perspectivas: a sua e a dele. Ou, se preferir, pode seguir diretamente para o presente e enfrentar sua jornada de cura."
    
    menu "Deseja revisitar as memórias do relacionamento?":
        "Sim, quero ver as memórias":
            jump flashback_menu
        "Não, seguir para o presente":
            jump presente

#########################################
# FLASHBACK – MEMÓRIAS DO PASSADO
#########################################

label flashback_menu:
    scene bg_flashback_intro with fade
    n "Reviver o passado pode ser doloroso, mas pode ajudar a compreender os abusos que marcaram sua história."
    menu "Escolha a perspectiva para as memórias:":
        "Perspectiva de Mia":
            jump flashback_mia
        "Perspectiva do Ex":
            jump flashback_ex

label flashback_mia:
    scene bg_flashback with dissolve
    m "Eu lembro claramente da primeira vez que ele entrou na minha vida. Minha família já intuía que ele não era o homem que me faria feliz."
    m "Minha mãe dizia que via nele uma arrogância e uma paranoia – como se ele achasse que ninguém se interessaria se ele mudasse."
    m "Durante meses, fui tratada como se não valesse nada. Os raros momentos de carinho eram ofuscados por insultos e manipulações."
    m "Lembro do dia em que ele exibiu fotos provocantes no Instagram e fez comentários que me deixaram devastada. Cada atitude reafirmava que eu estava presa a um ciclo de abuso."
    m "Na intimidade, ele ultrapassava os limites, insistindo mesmo quando eu não queria. Era como se o amor dele servisse apenas para justificar tudo."
    n "Essas memórias dolorosas permanecem, deixando cicatrizes invisíveis que ainda me atormentam."
    jump flashback_conclude

label flashback_ex:
    scene bg_flashback with dissolve
    ex "Eu sempre acreditei que o que tínhamos era especial, mas as críticas e rejeições me feriram profundamente."
    ex "Minha família via em mim uma arrogância que eu nem sabia possuir. Eu tentava demonstrar carinho, embora minhas atitudes muitas vezes saíssem erradas."
    ex "Usava as redes sociais para me afirmar, mesmo que de forma equivocada, e isso te magoava."
    ex "Na intimidade, pressionava você, na tentativa de manter nosso laço, mesmo sabendo que ultrapassava seus limites."
    ex "Quando você se afastou, tentei justificar meus erros, mas, no fundo, sabia que havia causado dor irreparável."
    n "Mesmo do meu lado, os erros foram inevitáveis. O passado se mostra difuso e doloroso para ambos."
    jump flashback_conclude

label flashback_conclude:
    n "As memórias revelam a complexidade de um relacionamento marcado por abusos e desentendimentos."
    n "Agora, é hora de voltar ao presente e enfrentar as cicatrizes invisíveis que ainda te acompanham."
    jump presente

#########################################
# PRESENTE – A JORNADA DE MIA
#########################################

label presente:
    scene bg_present with fade
    n "Você retorna ao presente. Mia, determinada a se libertar do ciclo de abuso, inicia sua jornada de cura."
    n "Sua história se desdobra em três atos: Prisão Invisível, Reconstrução e, finalmente, Libertação ou Retorno."
    jump ato1

#########################################
# ATO 1: PRISÃO INVISÍVEL
#########################################

label ato1:
    scene bg_prisao with fade
    n "ATO 1: Prisão Invisível"
    m "Mesmo após o fim, sinto que ele ainda está presente... uma sombra que se recusa a desaparecer."
    m "Pesadelos me perturbam, e a qualquer momento meu celular vibra com mensagens que me transportam para os piores momentos."
    
    menu "Seu celular vibra. O que você faz?":
        "Ignorar a mensagem":
            jump ato1_ignorar
        "Abrir a mensagem":
            jump ato1_abrir

label ato1_ignorar:
    m "Fecho os olhos, tentando ignorar a mensagem, mas a sensação de que algo maligno insiste em me alcançar não me abandona."
    m "A sombra do passado se aprofunda, e minhas cicatrizes parecem se reabrir."
    jump ato1_continue

label ato1_abrir:
    m "Respiro fundo e deslizo o dedo para abrir a mensagem. Na tela, palavras frias surgem: 'Você nunca vai me esquecer. Eu sempre estarei aqui.'"
    m "Essas palavras cortam fundo, reavivando a dor que tentei enterrar."
    jump ato1_continue

label ato1_continue:
    m "Cada decisão me leva mais fundo no abismo da insegurança. Minhas cicatrizes invisíveis se transformam em feridas abertas, e minha autoconfiança se esvai."
    menu "Como você reage neste momento de vulnerabilidade?":
        "Mergulhar na dor e reviver cada detalhe":
            jump ato1_detalhes
        "Procurar apoio para enfrentar essa escuridão":
            jump ato1_apoio

label ato1_detalhes:
    m "Deixo-me levar pela dor, revivendo cada humilhação, cada manipulação. As memórias se misturam, criando um turbilhão do qual parece não haver escape."
    jump ato2

label ato1_apoio:
    m "Decido que preciso de ajuda. Ligo para minha amiga, na esperança de encontrar um ombro que me lembre do meu valor."
    f "Mia, sei o quanto essa dor é profunda. Mas você é muito mais do que tudo isso. Lembre-se: você merece amor e respeito."
    m "Mesmo que as sombras do passado insistam em me assombrar, as palavras dela acendem uma centelha de esperança."
    jump ato2

#########################################
# ATO 2: RECONSTRUÇÃO
#########################################

label ato2:
    scene bg_reconstrucao with fade
    n "ATO 2: Reconstrução"
    m "Com o tempo, começo a enfrentar as sombras do passado. Cada novo dia é uma batalha para resgatar minha autoconfiança e redescobrir quem eu sou."
    m "Procuro apoio em amigos e familiares e tento criar novas memórias que possam contrastar com as cicatrizes invisíveis."
    
    menu "Durante esse processo, você decide:":
        "Enfrentar diretamente as lembranças dolorosas":
            jump ato2_enfrentar
        "Focar em construir novas experiências e memórias":
            jump ato2_novamemoria

label ato2_enfrentar:
    m "Determino enfrentar cada lembrança. Reviso fotos, mensagens e momentos difíceis, tentando compreender a origem da minha dor."
    m "Entretanto, a presença dele se manifesta de forma distorcida, tentando me puxar de volta ao ciclo do abuso."
    jump ato3

label ato2_novamemoria:
    m "Decido que é hora de construir algo novo. Procuro lugares, novas amizades e experiências que me façam sentir viva."
    m "Mesmo assim, de vez em quando, uma mensagem enigmática ou uma sombra familiar me lembra que o passado não se rende facilmente."
    jump ato3

#########################################
# ATO 3: LIBERTAÇÃO OU RETORNO
#########################################

label ato3:
    scene bg_libertacao with fade
    n "ATO 3: Libertação ou Retorno"
    m "Chego ao momento decisivo. Cada escolha que fiz me trouxe até aqui, e agora, o rumo da minha vida depende unicamente de mim."
    m "Diante da presença manipuladora do meu ex – que se ergue como uma entidade do meu passado – preciso decidir: seguir em frente ou ser arrastada de volta ao ciclo tóxico."
    
    menu "Escolha seu destino final:":
        "Final de Superação":
            jump final_superacao
        "Final de Enfrentamento":
            jump final_enfrentamento
        "Final de Recaída":
            jump final_recaida

label final_superacao:
    scene bg_final with fade
    m "Encontro forças dentro de mim que jamais imaginei possuir. Com o apoio daqueles que me amam, deixo para trás o ciclo de abuso."
    m "Cada cicatriz invisível se transforma em um símbolo da minha resiliência. Hoje, vivo com amor próprio e esperança."
    n "FINAL DE SUPERAÇÃO: Mia segue seu caminho, reconstruindo sua vida e deixando as sombras do passado para trás."
    jump fim

label final_enfrentamento:
    scene bg_final with fade
    m "Reúno toda a minha coragem e encaro de frente a entidade que representa o meu ex. Em um confronto doloroso, rompo os laços que me mantinham presa."
    m "Ao enfrentar o passado, afirmo minha autonomia e abro caminho para uma nova vida."
    n "FINAL DE ENFRENTAMENTO: Mia confronta seu passado e encerra o domínio que o ex exercia sobre sua mente, alcançando a verdadeira libertação."
    jump fim

label final_recaida:
    scene bg_final with fade
    m "Mesmo com tanto esforço, a dor e a insegurança se sobrepõem à minha vontade de mudar. Acabo retornando ao ciclo tóxico, acreditando que posso encontrar conforto naquele abismo."
    m "Cada dia se torna uma repetição dolorosa, onde a esperança se esvai e as cicatrizes invisíveis se aprofundam."
    n "FINAL DE RECAÍDA: Mia retorna ao relacionamento abusivo, aprisionada num ciclo do qual parece não haver escape."
    jump fim

#########################################
# FINAL DO JOGO
#########################################

label fim:
    scene bg_end with fade
    n "Obrigado por vivenciar 'Cicatrizes Invisíveis'. Cada escolha que você fez moldou o destino de Mia."
    n "Que essa história seja um lembrete da importância de reconhecer seu valor e buscar a verdadeira liberdade."
    return
