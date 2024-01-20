function goBack() {
    window.history.back();
}

function likeButtonPress(id){
    const url = '../like/'

    const requestOptions = {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: id
    };
    
    fetch(url, requestOptions);
    refreshLikeButton(id)
}

async function getLike(id){
    url = '../get_like/'+id
    return fetch(url).then((res)=>res.json())
}

async function refreshLikeButton(id){
    payload = await getLike(id)
    likes = payload['number_of_likes']
    isLike = payload['is_like']
    
    console.log(payload)
    if(isLike==false){
        document.getElementById('like-button').className = "btn btn-outline-primary"
    }
    else{
        document.getElementById('like-button').className = "btn btn-primary"
    }

    document.getElementById('number-of-likes').innerHTML = `(${likes})`;
    return isLike
}

const id = document.getElementById("content-id").innerHTML;
refreshLikeButton(id)