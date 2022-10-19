import {createApp} from 'vue';
import "bootstrap/dist/css/bootstrap.min.css";
import "bootstrap";
import "./assets/reset.css"
import App from './App.vue';
import router from "@/router";
import store from "@/store";
import Popper from "vue3-popper";
import { library } from "@fortawesome/fontawesome-svg-core";
import { faGraduationCap, faPenToSquare, faTrashCan, faChevronDown, faMagnifyingGlass  } from "@fortawesome/free-solid-svg-icons";
import { faSquareCaretDown } from "@fortawesome/free-regular-svg-icons";
import { faLinkedin, faGithub } from "@fortawesome/free-brands-svg-icons";
import { FontAwesomeIcon } from "@fortawesome/vue-fontawesome";



library.add(faGraduationCap, faSquareCaretDown, faPenToSquare, faTrashCan, faChevronDown, faMagnifyingGlass, faLinkedin, faGithub);

const app = createApp(App);

app.use(router);
app.use(store);
app.component("font-awesome-icon", FontAwesomeIcon);
app.component("Popper", Popper);

app.mount('#app');
