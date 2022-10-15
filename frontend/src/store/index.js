import { createStore } from "vuex";
import studentsModule from "@/store/modules/students";


const store = createStore({
    modules: {
        students: studentsModule
    }
});


export default store;