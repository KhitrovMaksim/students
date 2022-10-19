import mutations from "@/store/modules/students/mutations";
import actions from "@/store/modules/students/actions";
import getters from "@/store/modules/students/getters";


export default {
    namespaced: true,
    state() {
        return {
            students: [
                {
                    id: '1',
                    firstName: 'Maksim',
                    lastName: 'Khitrov',
                    dateOfBirth: '24/06/1985',
                    email: 'khitrov.maksim@reqres.in',
                    phone: '(111) 111-1111',
                    favoriteSports: ['Football', 'Tennis']
                },
                {
                    id: '2',
                    firstName: 'Michael',
                    lastName: 'Lawson',
                    dateOfBirth: '12/10/1970',
                    email: 'michael.lawson@reqres.in',
                    phone: '(999) 999-9999',
                    favoriteSports: ['Golf']
                }
            ]
        }
    },
    mutations,
    actions,
    getters
};