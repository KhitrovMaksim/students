import mutations from "@/store/modules/students/mutations";
import actions from "@/store/modules/students/actions";
import getters from "@/store/modules/students/getters";


export default {
    namespaced: true,
    state() {
        return {
            students: null
        }
    },
    mutations,
    actions,
    getters
};