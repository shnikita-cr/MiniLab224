const backendHost = "http://127.0.0.1:5000"
const apiPrefix = "/api/v1"
const apiURL = backendHost + apiPrefix
const githubPrefix = "/github"


export const getUserFollowers = (username) => {
  const xmlHttp = new XMLHttpRequest();
  xmlHttp.open( "GET", `${apiURL}${githubPrefix}/${username}`, false ); // false for synchronous request
  xmlHttp.send( null );
  return JSON.parse(xmlHttp.responseText)
}