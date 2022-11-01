export default {
    async getStudents() {
        try {
            let link = ""
            if (window.location.host === '127.0.0.1:8080' || window.location.host === 'localhost:8080')
                link = "http://localhost:8000/students/"
            else link = window.location.protocol + "//" + window.location.host + ":8080/students"
            const response = await fetch(link, {
                method: 'GET'
            })

            if (!response.ok) {
                throw new Error(`Error! status: ${response.status}`);
            }

            const result = await response.json();
            return result;
        } catch (err) {
            console.log(err);
        }
    },
    students(state, getters) {
        console.log(getters.getStudents)
        return state.students;
    },
    hasStudents(state) {
        return state.students && state.students.length > 0;
    },
    getStudentById: (state) => (id) => {
        return state.students.find(student => student.id === id)
    }
};