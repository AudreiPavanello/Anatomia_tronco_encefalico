import streamlit as st

# --- Configuração da Página ---
st.set_page_config(
    page_title="Neuroanatomia Interativa | Tronco Encefálico",
    page_icon="🧠",
    layout="wide"
)

# --- Dados dos Quizzes (com terminologia corrigida) ---

quiz_geral_data = [
    {
        "question": "O tronco encefálico se interpõe entre quais estruturas do sistema nervoso central?",
        "options": [
            "O telencéfalo e o cerebelo",
            "A medula espinal e o diencéfalo",
            "O córtex cerebral e a medula espinal",
            "O diencéfalo e o cerebelo"
        ],
        "answer": "A medula espinal e o diencéfalo",
        "explanation": "O tronco encefálico é a porção mais caudal do encéfalo, interpondo-se entre a medula espinal e o diencéfalo, e situando-se ventralmente ao cerebelo."
    },
    {
        "question": "Qual dos seguintes centros, localizado no bulbo, é responsável por controlar a vasoconstrição, a vasodilatação e a frequência cardíaca?",
        "options": [
            "Centro respiratório",
            "Centro do vômito",
            "Centro cardiovascular",
            "Núcleo olivar inferior"
        ],
        "answer": "Centro cardiovascular",
        "explanation": "O centro cardiovascular, localizado na formação reticular do bulbo, controla a vasoconstrição e a vasodilatação dos vasos sanguíneos, bem como a frequência e a intensidade dos batimentos cardíacos."
    },
    {
        "question": "Os núcleos grácil e cuneiforme, localizados no bulbo, são essenciais para quais tipos de sensibilidade?",
        "options": [
            "Dor e temperatura",
            "Propriocepção consciente, tato epicrítico e sensibilidade vibratória",
            "Audição e equilíbrio",
            "Paladar e olfato"
        ],
        "answer": "Propriocepção consciente, tato epicrítico e sensibilidade vibratória",
        "explanation": "Os núcleos grácil e cuneiforme recebem e processam informações de propriocepção consciente, tato epicrítico e sensibilidade vibratória, que depois seguem pelo lemnisco medial."
    },
    {
        "question": "Qual estrutura divide o mesencéfalo em uma porção posterior (teto) e uma porção anterior (pedúnculos cerebrais)?",
        "options": [
            "Quarto ventrículo",
            "Sulco basilar",
            "Aqueduto do mesencéfalo",
            "Fissura mediana anterior"
        ],
        "answer": "Aqueduto do mesencéfalo",
        "explanation": "O mesencéfalo apresenta uma cavidade central chamada aqueduto do mesencéfalo, que o divide em um teto (posterior) e os pedúnculos cerebrais (anteriores)."
    },
    {
        "question": "O Locus ceruleus, um núcleo da formação reticular, é composto por neurônios ricos em qual neurotransmissor e está associado a quais funções?",
        "options": [
            "Serotonina; ciclo vigília-sono e emoções",
            "Dopamina; recompensa e prazer",
            "Acetilcolina; contração muscular e memória",
            "Noradrenalina; atenção seletiva, vigília e aprendizado"
        ],
        "answer": "Noradrenalina; atenção seletiva, vigília e aprendizado",
        "explanation": "O Locus coeruleus é a principal fonte de noradrenalina no cérebro, desempenhando um papel crucial na atenção, alerta, aprendizado e humor."
    },
    {
        "question": "Na face anterior do bulbo, qual o nome da estrutura onde as fibras do trato corticospinal cruzam para o lado oposto do corpo?",
        "options": [
            "Pirâmides bulbares",
            "Olivas bulbares",
            "Decussação das pirâmides",
            "Sulco mediano anterior"
        ],
        "answer": "Decussação das pirâmides",
        "explanation": "A decussação das pirâmides é o ponto caudal no bulbo onde cerca de 85% das fibras motoras do trato corticospinal cruzam a linha média, o que explica por que um hemisfério cerebral controla o lado oposto do corpo."
    },
    {
        "question": "Qual estrutura do mesencéfalo, rica em neurônios dopaminérgicos, é fundamental para o controle motor e está classicamente associada à Doença de Parkinson quando degenera?",
        "options": [
            "Núcleo rubro",
            "Substância negra",
            "Colículo superior",
            "Área tegmental ventral"
        ],
        "answer": "Substância negra",
        "explanation": "A substância negra é essencial no circuito dos núcleos da base para o planejamento e execução de movimentos. A perda de seus neurônios dopaminérgicos é a principal causa dos sintomas motores na Doença de Parkinson."
    },
    {
        "question": "Os núcleos pontinos, localizados na base da ponte, retransmitem informações do córtex cerebral para o cerebelo através de qual grande feixe de fibras transversais?",
        "options": [
            "Pedúnculos cerebrais",
            "Pedúnculos cerebelares superiores",
            "Pedúnculos cerebelares médios",
            "Lemnisco medial"
        ],
        "answer": "Pedúnculos cerebelares médios",
        "explanation": "As fibras corticopontinas terminam nos núcleos pontinos. Estes, por sua vez, projetam fibras (fibras transversais) que cruzam a linha média e formam os pedúnculos cerebelares médios, conectando a ponte ao cerebelo e informando-o sobre o plano motor."
    },
    {
        "question": "Os colículos superiores e inferiores, que formam o teto do mesencéfalo, estão envolvidos no processamento reflexo de quais modalidades sensoriais, respectivamente?",
        "options": [
            "Auditiva e Visual",
            "Visual e Auditiva",
            "Tátil e Gustativa",
            "Olfativa e Visual"
        ],
        "answer": "Visual e Auditiva",
        "explanation": "Os colículos superiores são centros para reflexos visuais (ex: mover a cabeça em direção a um estímulo visual). Os colículos inferiores são parte da via auditiva, ajudando a localizar a origem dos sons."
    },
    {
        "question": "Qual é a principal função do Sistema Reticular Ativador Ascendente (SARA), uma extensa rede de neurônios que se projeta para o córtex cerebral?",
        "options": [
            "Controle da frequência cardíaca",
            "Manutenção da consciência e do estado de alerta",
            "Coordenação da deglutição",
            "Regulação do equilíbrio"
        ],
        "answer": "Manutenção da consciência e do estado de alerta",
        "explanation": "O SARA é responsável por manter o córtex cerebral 'ativado', sendo fundamental para a vigília e a consciência. Lesões extensas nesta área podem resultar em coma."
    }
]

quiz_clinico_data = [
    {
        "question": "Um paciente apresenta disartria (dificuldade de articular palavras), disfagia (dificuldade de engolir) e disfonia (rouquidão), além de desvio da língua para o lado da lesão quando protruída. Este conjunto de sinais sugere fortemente uma lesão em qual estrutura?",
        "options": [
            "Mesencéfalo, afetando o nervo oculomotor (III)",
            "Ponte, afetando o nervo facial (VII)",
            "Bulbo, afetando os nervos glossofaríngeo (IX), vago (X) e hipoglosso (XII)",
            "Cerebelo, afetando a coordenação motora"
        ],
        "answer": "Bulbo, afetando os nervos glossofaríngeo (IX), vago (X) e hipoglosso (XII)",
        "explanation": "Lesões no bulbo que afetam os núcleos dos nervos glossofaríngeo (IX), vago (X) e hipoglosso (XII) causam déficits na musculatura da faringe, laringe e língua, resultando nos sinais descritos."
    },
    {
        "question": "Uma mulher de 45 anos relata início súbito de vertigem intensa, zumbido no ouvido esquerdo e perda auditiva progressiva. A ressonância magnética revela um tumor comprimindo um nervo craniano na sua emergência do sulco bulbo-pontino. Qual nervo é o mais provavelmente afetado?",
        "options": [
            "Nervo Trigêmeo (V)",
            "Nervo Acessório (XI)",
            "Nervo Vestibulococlear (VIII)",
            "Nervo Troclear (IV)"
        ],
        "answer": "Nervo Vestibulococlear (VIII)",
        "explanation": "O nervo vestibulococlear (VIII) emerge na junção entre a ponte e o bulbo e é responsável pela audição e pelo equilíbrio. A compressão deste nervo causa diretamente os sintomas de vertigem, zumbido (tinnitus) e surdez."
    },
    {
        "question": "Um paciente sofre um pequeno AVC que afeta o mesencéfalo. No exame, observa-se que seu olho esquerdo está 'caído' (ptose), a pupila está dilatada e ele não consegue mover o olho para cima, para baixo ou medialmente. Qual nervo craniano foi lesionado?",
        "options": [
            "Nervo Abducente (VI)",
            "Nervo Óptico (II)",
            "Nervo Trigêmeo (V)",
            "Nervo Oculomotor (III)"
        ],
        "answer": "Nervo Oculomotor (III)",
        "explanation": "A lesão do nervo oculomotor (III), cujos núcleos se localizam no mesencéfalo, causa a paralisia da maioria dos músculos extrínsecos do olho, do músculo levantador da pálpebra (ptose) e do esfíncter da pupila (midríase)."
    },
    {
        "question": "Um paciente apresenta paralisia dos músculos da mímica facial à direita (não consegue sorrir, franzir a testa ou fechar o olho direito) e incapacidade de mover o olho direito lateralmente (abduzir). Esta combinação de déficits sugere uma lesão na ponte afetando quais nervos cranianos?",
        "options": [
            "Trigêmeo (V) e Facial (VII)",
            "Abducente (VI) e Facial (VII)",
            "Vestibulococlear (VIII) e Glossofaríngeo (IX)",
            "Oculomotor (III) e Troclear (IV)"
        ],
        "answer": "Abducente (VI) e Facial (VII)",
        "explanation": "Lesões na ponte podem facilmente afetar estruturas próximas. A paralisia do músculo reto lateral do olho é causada por lesão no nervo abducente (VI), enquanto a paralisia facial periférica é causada por lesão no nervo facial (VII)."
    },
    {
        "question": "Uma lesão extensa e bilateral da formação reticular na porção superior da ponte e mesencéfalo, causada por um trauma ou hemorragia, provavelmente resultará em qual estado clínico?",
        "options": [
            "Paralisia facial completa",
            "Perda da sensibilidade vibratória",
            "Estado de coma",
            "Surdez bilateral"
        ],
        "answer": "Estado de coma",
        "explanation": "A formação reticular contém o Sistema Reticular Ativador Ascendente (SARA), que é essencial para manter a consciência. Uma lesão grave e bilateral desta área interrompe a ativação do córtex cerebral, levando ao coma."
    },
    {
        "question": "Um paciente chega ao pronto-socorro com vertigem, dificuldade para engolir (disfagia), rouquidão e perda da sensação de dor e temperatura no lado esquerdo do rosto e no lado direito do corpo. Este padrão cruzado de déficits é característico de uma oclusão arterial afetando a porção lateral de qual estrutura?",
        "options": [
            "Ponte (Síndrome de Millard-Gubler)",
            "Mesencéfalo (Síndrome de Weber)",
            "Bulbo (Síndrome de Wallenberg)",
            "Tálamo"
        ],
        "answer": "Bulbo (Síndrome de Wallenberg)",
        "explanation": "Esta é a apresentação clássica da Síndrome de Wallenberg (ou Síndrome Medular Lateral), que afeta o trato espinotalâmico (perda de sensibilidade contralateral no corpo) e o núcleo do trato espinal do trigêmeo (perda de sensibilidade ipsilateral na face), entre outras estruturas laterais do bulbo."
    },
    {
        "question": "Um paciente com histórico de hipertensão arterial apresenta fraqueza no lado direito do corpo (hemiparesia) e um desvio do olho esquerdo para 'baixo e para fora', com a pupila esquerda dilatada. Essa 'hemiplegia alternada' aponta para uma lesão no lado esquerdo de qual parte do tronco encefálico?",
        "options": [
            "Bulbo",
            "Ponte",
            "Mesencéfalo",
            "Cerebelo"
        ],
        "answer": "Mesencéfalo",
        "explanation": "Esta é a Síndrome de Weber. A lesão ocorre na base do pedúnculo cerebral esquerdo, afetando as fibras do trato corticospinal (causando hemiparesia direita) e as fibras do nervo oculomotor (III) (causando paralisia oculomotora ipsilateral)."
    },
    {
        "question": "A incapacidade de um paciente franzir a testa e sorrir no lado esquerdo da face, combinada com uma perda do paladar nos dois terços anteriores da língua no mesmo lado, sugere uma lesão de qual nervo craniano?",
        "options": [
            "Nervo Trigêmeo (V)",
            "Nervo Facial (VII)",
            "Nervo Glossofaríngeo (IX)",
            "Nervo Hipoglosso (XII)"
        ],
        "answer": "Nervo Facial (VII)",
        "explanation": "O nervo facial (VII) é responsável pela inervação dos músculos da expressão facial (função motora) e pela sensação gustativa dos dois terços anteriores da língua (função sensorial especial). Uma lesão periférica deste nervo causa ambos os déficits no mesmo lado."
    },
     {
        "question": "Um paciente apresenta paralisia do palato mole ('queda do véu palatino') e dificuldade para engolir. Ao exame, o reflexo do vômito está ausente. Qual nervo craniano, cujo núcleo ambíguo se localiza no bulbo, é o principal responsável por estes déficits?",
        "options": [
            "Nervo Trigêmeo (V)",
            "Nervo Facial (VII)",
            "Nervo Vago (X)",
            "Nervo Hipoglosso (XII)"
        ],
        "answer": "Nervo Vago (X)",
        "explanation": "O nervo vago (X) inerva a maior parte da musculatura da faringe e do palato mole, sendo essencial para a deglutição e a fonação. Ele também compõe a via eferente do reflexo do vômito. Lesões causam os sintomas descritos."
    },
    {
        "question": "Após um acidente, um paciente é incapaz de virar a cabeça para a esquerda contra resistência e não consegue elevar (encolher) o ombro direito. Isso indica uma lesão de qual nervo craniano?",
        "options": [
            "Nervo Vago (X)",
            "Nervo Acessório (XI)",
            "Nervo Hipoglosso (XII)",
            "Nervo Trigêmeo (V)"
        ],
        "answer": "Nervo Acessório (XI)",
        "explanation": "O nervo acessório (XI) inerva os músculos esternocleidomastóideo (que vira a cabeça para o lado oposto) e trapézio (que eleva o ombro). Uma lesão à direita causaria fraqueza para virar a cabeça para a esquerda e para encolher o ombro direito."
    }
]

# --- Funções do Quiz ---

def run_quiz(quiz_data, quiz_title):
    st.header(quiz_title, divider='blue')

    # Inicializar o estado da sessão para este quiz
    if f'{quiz_title}_current_question' not in st.session_state:
        st.session_state[f'{quiz_title}_current_question'] = 0
        st.session_state[f'{quiz_title}_score'] = 0
        st.session_state[f'{quiz_title}_answered'] = False
        st.session_state[f'{quiz_title}_user_answer'] = None

    q_index = st.session_state[f'{quiz_title}_current_question']

    if q_index < len(quiz_data):
        item = quiz_data[q_index]
        st.subheader(f"Questão {q_index + 1}/{len(quiz_data)}")
        st.markdown(f"**{item['question']}**")

        # Exibe as opções
        user_answer = st.radio("Escolha uma opção:", item['options'], key=f'{quiz_title}_{q_index}')
        
        # Se a pergunta ainda não foi respondida, mostre o botão de confirmar.
        if not st.session_state[f'{quiz_title}_answered']:
            if st.button("Confirmar Resposta", key=f'submit_{quiz_title}_{q_index}'):
                st.session_state[f'{quiz_title}_user_answer'] = user_answer
                if user_answer == item['answer']:
                    st.session_state[f'{quiz_title}_score'] += 1
                st.session_state[f'{quiz_title}_answered'] = True
                st.rerun()

        # Se a pergunta JÁ FOI respondida, mostre a justificativa e o botão de próxima.
        if st.session_state[f'{quiz_title}_answered']:
            user_ans = st.session_state[f'{quiz_title}_user_answer']
            if user_ans == item['answer']:
                st.success(f"Correto! A resposta é: **{item['answer']}**")
            else:
                st.error(f"Incorreto. Você marcou '{user_ans}'. A resposta correta é: **{item['answer']}**")
            st.info(f"**Justificativa:** {item['explanation']}")

            if st.button("Próxima Pergunta", key=f'next_{quiz_title}_{q_index}'):
                st.session_state[f'{quiz_title}_current_question'] += 1
                st.session_state[f'{quiz_title}_answered'] = False
                st.session_state[f'{quiz_title}_user_answer'] = None
                st.rerun()

    else:
        score = st.session_state[f'{quiz_title}_score']
        total = len(quiz_data)
        st.success(f"Quiz finalizado! Sua pontuação: **{score}/{total}**")
        st.balloons()
        if st.button("Recomeçar Quiz", key=f'restart_{quiz_title}'):
            st.session_state[f'{quiz_title}_current_question'] = 0
            st.session_state[f'{quiz_title}_score'] = 0
            st.session_state[f'{quiz_title}_answered'] = False
            st.session_state[f'{quiz_title}_user_answer'] = None
            st.rerun()

# --- Interface Principal ---

st.title("🧠 Anatomia Interativa do Tronco Encefálico")

# --- Menu Lateral ---
st.sidebar.title("Navegação")
selection = st.sidebar.radio("Selecione uma seção:", ["Material de Estudo", "Quiz Geral", "Quiz Clínico"])

# --- Conteúdo das Seções (com terminologia corrigida) ---

if selection == "Material de Estudo":
    st.header("Material de Estudo 📚", divider='blue')
    st.markdown("Utilize esta seção para revisar os principais pontos da anatomia e função do tronco encefálico.")

    with st.expander("Bulbo"):
        st.markdown("""
        - **Localização:** É a porção mais caudal, contínua com a medula espinal. Inicia-se no forame magno e estende-se até a ponte.
        - **Função Principal:** Conecta o encéfalo à medula espinal.
        - **Centros Vitais (na Formação Reticular):**
            - **Centro Cardiovascular:** Controla a frequência cardíaca e o diâmetro dos vasos sanguíneos.
            - **Centro Respiratório:** Controla o ritmo básico da respiração.
            - **Centro do Vômito:** Controla o reflexo do vômito.
        - **Estruturas Externas Importantes:**
            - **Pirâmides Bulbares:** Contêm o trato corticospinal.
            - **Decussação das Pirâmides:** Ponto onde as fibras do trato corticospinal cruzam para o lado oposto.
            - **Olivas:** Elevações laterais às pirâmides, relacionadas ao aprendizado motor.
        - **Núcleos Próprios Importantes:**
            - **Núcleos Grácil e Cuneiforme:** Recebem informações de propriocepção consciente, tato epicrítico e sensibilidade vibratória.
            - **Complexo Olivar Inferior:** Envia eferências para o cerebelo, participando da aprendizagem motora.
        """)

    with st.expander("Ponte"):
        st.markdown("""
        - **Localização:** Situada superiormente ao bulbo e ventralmente ao cerebelo.
        - **Estrutura:** Dividida em uma região ventral (base da ponte) e uma dorsal (tegmento da ponte).
        - **Funções Principais:**
            - **Conexão de Vias Motoras:** Atua como uma "ponte" que conecta vias motoras, ajudando a coordenar e otimizar a atividade motora voluntária.
            - **Controle Respiratório:** Possui um centro respiratório que atua em conjunto com o centro do bulbo.
        - **Estruturas Importantes:**
            - **Núcleos Pontinos:** Localizados na base, retransmitem informações do córtex cerebral para o cerebelo.
            - **Pedúnculos Cerebelares Médios:** Fibras transversais que se originam nos núcleos pontinos e se projetam para o cerebelo.
            - **Núcleos de Nervos Cranianos:** Contém núcleos dos nervos Trigêmeo (V), Abducente (VI), Facial (VII) e Vestibulococlear (VIII).
        """)

    with st.expander("Mesencéfalo"):
        st.markdown("""
        - **Localização:** Posicionado entre a ponte e o diencéfalo.
        - **Estrutura:** Atravessado pelo **aqueduto do mesencéfalo**, que o divide em:
            - **Teto do Mesencéfalo (posterior):** Contém os colículos superiores e inferiores.
            - **Pedúnculos Cerebrais (anterior):** Cada um dividido em base e tegmento.
        - **Funções e Estruturas Importantes:**
            - **Colículos Superiores:** Envolvidos em reflexos visuais.
            - **Colículos Inferiores:** Parte da via auditiva.
            - **Substância Negra:** Essencial para o controle motor; sua degeneração está associada à Doença de Parkinson.
            - **Núcleo Rubro:** Participa da coordenação motora.
            - **Núcleos de Nervos Cranianos:** Contém núcleos dos nervos Oculomotor (III) e Troclear (IV).
        """)
    
    with st.expander("Formação Reticular"):
        st.markdown("""
        - **Definição:** Uma rede complexa de substância cinzenta e branca que se estende por todo o tronco encefálico.
        - **SARA (Sistema Reticular Ativador Ascendente):**
            - **Função:** Mantém o córtex cerebral em estado de alerta e consciência.
            - **Ativação:** É ativado por diversos estímulos sensoriais (visuais, auditivos, táteis, etc.).
            - **Clínica:** Lesões extensas na formação reticular podem levar ao estado de coma.
        - **Núcleos Principais:**
            - **Núcleos da Rafe:** Ricos em serotonina, regulam o ciclo vigília-sono, humor e outras funções.
            - **Locus ceruleus:** Rico em noradrenalina, envolvido na atenção, vigília e aprendizado.
            - **Área Tegmental Ventral:** Rica em dopamina, central no sistema de recompensa e prazer.
        - **Outras Funções:** Controle da motricidade, sensibilidade (incluindo dor), sistema nervoso autônomo e integração de reflexos.
        """)

elif selection == "Quiz Geral":
    run_quiz(quiz_geral_data, "Quiz Geral")

elif selection == "Quiz Clínico":
    run_quiz(quiz_clinico_data, "Quiz Clínico")

st.sidebar.markdown("---")
st.sidebar.info("Desenvolvido com base em Machado - Neuroanatomia Funcional - 4° Edição'")