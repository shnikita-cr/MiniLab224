import * as css from './index.css'
import Viva from "vivagraphjs";


export default class App {
  constructor (elem) {
    if (!elem) return
    this.elem = elem
    this.defaultIconSize = 50
    this.defaultURL = "https://ibb.co/68dTG9c"
    
    this.graphics = Viva.Graph.View.svgGraphics();
    this.graphics.node(function(node) {
     // The function is called every time renderer needs a ui to display node
     return Viva.Graph.svg('image')
           .attr('width', node.data["size"])
           .attr('height', node.data["size"])
           .link((node.data && node.data.url))
      // node.data holds custom object passed to graph.addNode();
      })
      .placeNode(function(nodeUI, pos){
          // Shift image to let links go to the center:
          nodeUI.attr('x', pos.x - 12).attr('y', pos.y - 12);
      });
  }
  
  addNodesToGraph (root_user, followers, graph) {
    const getDataFromPerson = (person) => {
      return {url : person["avatar_url"] || this.defaultURL, size: person["size"] || this.defaultIconSize}
    }
    
    graph.addNode(root_user, getDataFromPerson({"login": root_user}))
    
    for (const person of followers) {
      if (!graph.getNode(person["login"])) {
        graph.addNode(person["login"], getDataFromPerson(person))
      }
      graph.addLink(root_user, person["login"]);
      if (person["followers"] !== undefined) {
        this.addNodesToGraph(person["login"], person["followers"], graph)
      }
    }
  }

  render (root_user, followers) {
    const graph = Viva.Graph.graph()
    this.addNodesToGraph(root_user, followers, graph)
    
    const layout = Viva.Graph.Layout.forceDirected(graph, {
      springLength : followers && followers.length * 2 || 200,
      springCoeff : 0.00001,
      dragCoeff : 0.002,
      gravity : -112.5
    });

    const renderer = Viva.Graph.View.renderer(graph, {
      container: document.querySelector(".graph-container"),
      layout: layout,
      graphics : this.graphics
    });
    renderer.run()
  }
}