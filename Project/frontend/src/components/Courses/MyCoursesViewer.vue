<template>
  <v-container class="my-5">
    <v-card v-for="(course, index) in info" :key="course.name">
      <v-layout row wrap class="pa-6">
        <!-- <v-flex xs4 sm4 md2 d-flex>
            <v-img :src="require('../assets/' + course.name + '.png')"></v-img>
          </v-flex> -->
        <v-flex xs3 sm2 md2>
          <div class="caption grey--text">Course Name</div>
          <div>{{ course.name }}</div>
        </v-flex>
        <v-flex xs3 sm2 md2>
          <div class="caption grey--text">Year</div>
          <div>{{ course.year_code }}</div>
        </v-flex>
        <v-flex xs3 sm2 md2>
          <div class="caption grey--text">Student Count</div>
          <div>{{ course.student_count }}</div>
        </v-flex>
        <v-flex xs3 sm2 md2>
          <div class="caption grey--text">Date Updated</div>
          <div>{{ showDate(course.date_updated) }}</div>
        </v-flex>
          <v-flex xs3 sm2 md2>
          <div class="caption grey--text">Go to course page</div>
          <v-icon style="cursor:pointer" @click="navToCourseCategorySelection(course.name,course.id)"
            >find_in_page</v-icon
          >
        </v-flex>
        <v-flex xs3 sm2 md2>
          <div class="caption grey--text">Unregirster Course</div>
          <v-icon style="cursor:pointer" @click="RemoveCourse(course.id, index)"
            >delete</v-icon
          >
        </v-flex>
      </v-layout>
      <v-divider></v-divider>
    </v-card>
  </v-container>
</template>
// courses should be an array of { name: , lecturer: , rank: , courseStage: ,
school:}
<script>
export default {
  props: ["info"],
  methods: {
      showDate: function (date){
            return date.split('T')[0]
        },
    navToCourseCategorySelection(nameOfCourse, id) {
      return this.$router.push({
        name: "CourseCategorySelection",
        params: { courseName: nameOfCourse, courseID: id },
      });
    },
    RemoveCourse(courseID, index) {
      var data = { course_id: courseID };

      var url = "http://localhost:8000/course/deregister/";

      this.$http.post(url, data).then((response) => console.log(response.data));
      //remove from list
      this.info.splice(index, 1)
      // this.info.remove(index);
    },
  },
};
</script>

<style></style>
