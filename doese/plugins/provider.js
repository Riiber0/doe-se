import Vue from "vue";
import { OpenStreetMapProvider } from 'leaflet-geosearch';
import "leaflet/dist/leaflet.css";

export default ({ app }, inject) => {
    // Inject $hello(msg) in Vue, context and store.
    inject('osm', new OpenStreetMapProvider())
  }