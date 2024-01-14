async function getRandomPokemon() {
    let response = await fetch('http://127.0.0.1:5000/get-random-pokemon');
    let pokemon = await response.json(); //extract JSON from the http response

    let name = pokemon[0];
    let img_path = pokemon[1];
    let type01 = pokemon[2];
    let type02 = pokemon[3];

    document.querySelector("#name").innerHTML = name;
    document.querySelector("#pokemon-img").src = img_path;
    document.querySelector("#type01").innerHTML = type01;
    document.querySelector("#type02").innerHTML = type02;

}