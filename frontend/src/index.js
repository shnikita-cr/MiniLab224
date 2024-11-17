/**
 * The entry point
 */

import App from './components/app'
import {getUserFollowers} from "./api/requests";




const updateName = (app, name) => {
    const followers = getUserFollowers(name)
    app.render(name, followers)
}


window.addEventListener('load', () => {
  const app = new App(document.getElementById('app'))
  const input = document.getElementById('input')

  input.onchange  = (e) => updateName(app, e.target.value)
  
  // Дефолтное значение для username
  updateName(app, "x4nth055")

})