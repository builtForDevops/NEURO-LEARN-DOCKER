<template>
  <div style="text-align: center">
    <div style="margin: 0px auto; text-align: left; padding: 14px 14px 14px 28px; color: #505050; width: 786px">
      <h3>Overview</h3>
      <el-row>
        <el-col :span="4" :offset=".5">
          <el-card :body-style="{ padding: '0px' }" style="background-color: #FFFFFF; width: 90%">
            <div style="padding: 14px; color: #282828; text-align: center">
              <h4>Total</h4>
              <div>
                <h1>{{ total_num }}</h1>
              </div>
            </div>
          </el-card>
        </el-col>
        <el-col :span="4" :offset="1">
          <el-card :body-style="{ padding: '0px' }" style="background-color: #FFFFFF; width: 90%">
            <div style="padding: 14px; color: #006699; text-align: center">
              <h4>Submitted</h4>
              <div>
                <h1>{{ submitted_num }}</h1>
              </div>
            </div>
          </el-card>
        </el-col>
        <el-col :span="4" :offset="1">
          <el-card :body-style="{ padding: '0px' }" style="background-color: #FFFFFF; width: 90%">
            <div style="padding: 14px; color: #00CCFF; text-align: center">
              <h4>Running</h4>
              <div>
                <h1>{{ running_num }}</h1>
              </div>
            </div>
          </el-card>
        </el-col>
        <el-col :span="4" :offset="1">
          <el-card :body-style="{ padding: '0px' }" style="background-color: #FFFFFF; width: 90%">
            <div style="padding: 14px; color: #00CC99; text-align: center">
              <h4>Finished</h4>
              <div>
                <h1>{{ finished_num }}</h1>
              </div>
            </div>
          </el-card>
        </el-col>
        <el-col :span="4" :offset="1">
          <el-card :body-style="{ padding: '0px' }" style="background-color: #FFFFFF; width: 90%">
            <div style="padding: 14px; color: #FF3333; text-align: center">
              <h4>Failed</h4>
              <div>
                <h1>{{ failed_num }}</h1>
              </div>
            </div>
          </el-card>
        </el-col>
      </el-row>
    </div>
    <div style="margin: 0px auto; text-align: left; padding: 0px 28px 14px 28px; color: #505050; width: 772px">
      <h3>Recent</h3>
      <el-tabs style="background-color: #FFFFFF; padding: 14px" el-tabs @tab-click="handleTabClick" stretch v-model="tabsValue">
        <!-- <el-tab-pane label="Statistical Analysis" name="Statistical Analysis">
          <el-table
            class="submissions-table"
            :data="submissions_table"
            stripe
            border
            @row-dblclick="onRowClick"
            style="width: 100%; background-color: #E8E8E8; color: #282828"
            :default-sort = "{prop: 'fields.task_id', order: 'descending'}">
            <el-table-column type="expand">
              <template slot-scope="props">
                <el-form label-position="left" inline class="demo-table-expand">
                    <el-form-item label="Task ID">
                      <span>{{ props.row.fields.task_id }}</span>
                    </el-form-item>
                    <el-form-item label="Proj. Name">
                      <span>{{ props.row.fields.project_name }}</span>
                    </el-form-item>
                    <el-form-item label="Test Var. / Data X">
                      <span>{{ props.row.fields.test_var_data_x }}</span>
                    </el-form-item>
                    <el-form-item label="Group Var. / Data Y">
                      <span>{{ props.row.fields.group_var_data_y }}</span>
                    </el-form-item>
                    <el-form-item label="Note">
                      <span>{{ props.row.fields.note }}</span>
                    </el-form-item>
                  </el-form>
              </template>
            </el-table-column>
            <el-table-column
            label="Task Name"
            prop="fields.task_name">
            </el-table-column>
            <el-table-column
            label="Task Type"
            prop="fields.task_type"
            width="120">
            </el-table-column>
            <el-table-column
            label="Status"
            prop="fields.task_status"
            width="100">
              <template slot-scope="scope">
                <el-tag
                  size="small"
                  :type="scope.row.fields.task_status === 'Finished' ? 'success' : (scope.row.fields.task_status === 'Failed' ? 'danger' : (scope.row.fields.task_status === 'Running' ? 'primary' : 'info'))">
                  {{ scope.row.fields.task_status }}
                </el-tag>
              </template>
            </el-table-column>
          </el-table>
        </el-tab-pane> -->
        <el-tab-pane label="Machine Learning" name="Machine Learning">
          <el-table
            class="submissions-table"
            :data="submissions_table"
            stripe
            border
            @row-dblclick="onRowClick"
            style="width: 100%; background-color: #E8E8E8; color: #282828"
            :default-sort = "{prop: 'fields.task_id', order: 'descending'}">
            <el-table-column type="expand">
              <template slot-scope="props">
                <el-form label-position="left" inline class="demo-table-expand">
                  <el-form-item label="Task ID">
                    <span>{{ props.row.fields.task_id }}</span>
                  </el-form-item>
                  <el-form-item label="Proj. Name">
                    <span>{{ props.row.fields.proj_name }}</span>
                  </el-form-item>
                  <el-form-item label="Train Data">
                    <span>{{ props.row.fields.train_data }}</span>
                  </el-form-item>
                  <el-form-item label="Test Data">
                    <span>{{ props.row.fields.test_data }}</span>
                  </el-form-item>
                  <el-form-item label="Label">
                    <span>{{ props.row.fields.label }}</span>
                  </el-form-item>
                  <el-form-item label="Feat. Sel.">
                    <span>{{ props.row.fields.feat_sel }}</span>
                  </el-form-item>
                  <el-form-item label="Estimator">
                    <span>{{ props.row.fields.estimator }}</span>
                  </el-form-item>
                  <el-form-item label="CV Type">
                    <span>{{ props.row.fields.cv_type }}</span>
                  </el-form-item>
                </el-form>
              </template>
            </el-table-column>
            <el-table-column
            label="Task Name"
            prop="fields.task_name">
            </el-table-column>
            <el-table-column
            label="Task Type"
            prop="fields.task_type"
            width="120">
            </el-table-column>
            <el-table-column
            label="Status"
            prop="fields.task_status"
            width="100">
              <template slot-scope="scope">
                <el-tag
                  size="small"
                  :type="scope.row.fields.task_status === 'Finished' ? 'success' : (scope.row.fields.task_status === 'Failed' ? 'danger' : (scope.row.fields.task_status === 'Running' ? 'primary' : 'info'))">
                  {{ scope.row.fields.task_status }}
                </el-tag>
              </template>
            </el-table-column>
          </el-table>
        </el-tab-pane>
      </el-tabs>
    </div>
</div>
</template>

<style>
  .clearfix:before,
  .clearfix:after {
      display: table;
      content: "";
  }
  .clearfix:after {
      clear: both
  }
  .el-carousel__item h3 {
    color: #3e4b5c;
    font-size: 14px;
    opacity: 0.75;
    line-height: 200px;
    margin: 0;
  }
  .el-carousel__item:nth-child(2n) {
    background-color: #8b9aaf;
  }
  .el-carousel__item:nth-child(2n+1) {
    background-color: #d3dce6;
  }
</style>

<script>
import axios from 'axios'
export default {
  data () {
    return {
      total_num: 0,
      tabsValue: 'Machine Learning',
      analysisType: 'Machine Learning',
      submitted_num: 0,
      running_num: 0,
      finished_num: 0,
      failed_num: 0,
      search_input: '',
      selected_status: '',
      submissions_table: []
    }
  },
  mounted: function () {
    this.showSubmissions()
  },
  methods: {
    showSubmissions () {
      axios.get('/api/v0/overview_submissions?analysis_type=' + this.analysisType)
        .then(response => {
          var res = response.data
          if (res.error_num === 0) {
            this.parseSubmissionsTable(res['list'])
            this.total_num = res['total_num']
            this.submitted_num = res['submitted_num']
            this.running_num = res['running_num']
            this.finished_num = res['finished_num']
            this.failed_num = res['failed_num']
          } else {
            this.$message.error('Failed!')
            console.log(res['msg'])
          }
        })
    },
    parseSubmissionsTable (submissions) {
      var parsedConfig
      if (this.analysisType === 'Machine Learning') {
        for (let submission of submissions) {
          parsedConfig = JSON.parse(submission.fields.task_config)
          submission.fields.proj_name = parsedConfig.proj_name
          submission.fields.train_data = parsedConfig.train_data
          submission.fields.test_data = parsedConfig.test_data
          submission.fields.label = parsedConfig.label
          submission.fields.feat_sel = parsedConfig.feat_sel
          submission.fields.estimator = parsedConfig.estimator
          submission.fields.cv_type = parsedConfig.cv_type
        }
      } else if (this.analysisType === 'Statistical Analysis') {
        for (let submission of submissions) {
          parsedConfig = JSON.parse(submission.fields.task_config)
          submission.fields.proj_name = parsedConfig.proj_name
          submission.fields.test_var_data_x = parsedConfig.group_var_data_y
          submission.fields.group_var_data_y = parsedConfig.group_var_data_y
        }
      }
      this.submissions_table = submissions
      console.log(this.submissions_table)
    },
    handleTabClick () {
      this.analysisType = this.tabsValue
      this.showSubmissions()
    },
    onRowClick (row) {
      this.$router.push({
        path: '/analysis/viewer',
        query: {taskid: row.fields.task_id, tasktype: row.fields.task_type, analysisType: this.analysisType}
      })
    }
  }
}
</script>
