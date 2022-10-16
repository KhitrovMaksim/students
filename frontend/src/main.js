import {createApp} from 'vue';
import "bootstrap/dist/css/bootstrap.min.css";
import "bootstrap";
import App from './App.vue';
import router from "@/router";
import { library } from "@fortawesome/fontawesome-svg-core";
import { faGraduationCap } from "@fortawesome/free-solid-svg-icons";
import { FontAwesomeIcon } from "@fortawesome/vue-fontawesome";


library.add(faGraduationCap);

const app = createApp(App);

app.use(router);
app.component("font-awesome-icon", FontAwesomeIcon)

app.mount('#app');
