document.addEventListener("DOMContentLoaded", function(){
    const inputField = document.getElementById("input-catalog-name");
    const type = document.getElementById("type").innerHTML;

    inputField.addEventListener("keydown", function (event) {
        if (event.key === "Enter") {
            refreshContents(type, inputField.value);
        }
    });

    async function findContentByTypeAndName(type, name) {
        url = type+'/'+name
        return fetch(url).then((res)=>res.json())
    }

    async function findAllContentByType(type) {
        url = 'getallbytype/'+type
        return fetch(url).then((res)=>res.json())
    }

    async function refreshContents(type, name){
        if(name==''){
            contents = await findAllContentByType(type)
        }
        else{
            contents = await findContentByTypeAndName(type, name)
        }
        document.getElementById("card-container").innerHTML=""
        let htmlString = ''

        if(contents.length == 0){
            document.getElementById("contents-notif").innerHTML = "The content you're looking for is not found :&lpar;"
        }
        else{
            document.getElementById("contents-notif").innerHTML = ""
            contents.forEach((item)=>{
                htmlString += `
                <a href="/content/${item.pk}">
                    <div class="col">    
                        <div class="card text-bg-dark" id="catalog-img-container">
                            <img src="${item.fields.resource}" class="card-img-top">
                            <div class="card-img-overlay">
                                <h5 class="card-title" id="card-content-text">${item.fields.name}</h5>
                            </div>
                        </div>
                    </div>
                </a>`
              })
        }
        document.getElementById("card-container").innerHTML = htmlString
    }
    refreshContents(type, '')
})