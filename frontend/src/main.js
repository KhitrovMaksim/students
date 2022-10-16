import {createApp} from 'vue';
import "bootstrap/dist/css/bootstrap.min.css";
import "bootstrap";
import App from './App.vue';
import router from "@/router";
import store from "@/store";
import Popper from "vue3-popper";
import { library } from "@fortawesome/fontawesome-svg-core";
import { faGraduationCap, faPen  } from "@fortawesome/free-solid-svg-icons";
import { faSquareCaretDown } from "@fortawesome/free-regular-svg-icons";
import { FontAwesomeIcon } from "@fortawesome/vue-fontawesome";



library.add(faGraduationCap, faSquareCaretDown, faPen);

const app = createApp(App);

app.use(router);
app.use(store);
app.component("font-awesome-icon", FontAwesomeIcon);
app.component("Popper", Popper);

app.mount('#app');
