/*

-> Página web que sempre que é carregada ou recarregada, mostra a frase atual do cache (do backend) como mensagem central.

-> Possui dois botões, um para refresh somente da frase e outro para change do conteúdo

-> Componentes
- p: main-content-phrase         -> conteúdo da frase atual do cache
- button: refresh-content-phrase -> força refresh do conteudo do 'main-content-phrase'
- button: change-content-phrase  -> força change e refresh do conteudo do 'main-content-phrase'

*/

// Global vars
URL_BASE = "http://localhost/api"


// UI elements
const button_refresh_content_phrase = document.getElementById("refresh-content-phrase");
const button_change_content_phrase = document.getElementById("change-content-phrase");
const p_main_content_phrase = document.getElementById("main-content-phrase");


// Listeners
button_refresh_content_phrase.addEventListener("click", refreshContentPhrase);
button_change_content_phrase.addEventListener("click", changeContentPhrase);
window.addEventListener("load", refreshContentPhrase);


// Functions
async function getCurrentPhrase() {
    const url = URL_BASE + "/get-current-phrase";
    let response, response_content;
    
    try {
        response = await fetch(url, {
            method: "GET",
            headers: { "Accept": "application/json" }
        });

        if (!response.ok) {
            throw Error("Response is not the expected");
        }

        response_content = await response.json();

        if (typeof response_content.current_phrase != "string") {
            throw Error("Response data type is not the expected");
        }

    } catch (err) {
        console.log(err);
        return ""
    }   

    console.log(response);

    return response_content.current_phrase;
}

async function refreshContentPhrase() {
    let current_cached_phrase = await getCurrentPhrase();

    p_main_content_phrase.textContent = current_cached_phrase;
}

async function changeContentPhrase() {
    const url = URL_BASE + "/change-current-phrase";
    let response;
    
    try {
        response = await fetch(url, {
            method: "GET",
            headers: { "Accept": "application/json" }
        });

        if (!response.ok) {
            throw Error("Response is not the expected");
        }
    } catch (err) {
        console.log(err);
        return ""
    }   
    console.log(response);
    
    refreshContentPhrase();
}
