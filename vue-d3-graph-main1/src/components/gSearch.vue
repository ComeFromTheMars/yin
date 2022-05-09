<template>
  <div style="margin-top: 20px;width: 500px;">
    <!-- <el-button style="margin-top: 15px;" @click="query">图数据切换，动态更新</el-button> -->
    <el-input
      style="width: 500px"
      class="inline-input"
      v-model="input"
      placeholder="请输入内容"
      clearable
      @keydown.enter.native="query"
    >
      <!-- <el-select
        v-model="mode"
        slot="prepend"
        placeholder="关键字查询"
      >
        <el-option label="关键字查询" value="1"></el-option>
        <el-option label="单实体查询" value="2"></el-option>
        <el-option label="关联查询" value="3"></el-option>
      </el-select>  -->
      <el-button
        slot="append"
        type="success"
        icon="el-icon-search"
        @click="query"
      >搜索</el-button>
    </el-input>
  </div>
</template>

<script>
export default {
  name: 'gSearch',
  data () {
    return {
      input: '',
      mode: '1',
      // 后台请求到的json数据
      data: []
    }
  },
  mounted () {
    this.$emit('getData', this.data)
  },
  methods: {
    query () {
      this.data = this.input
      this.$emit('getData', this.data)
    }
    // 模拟加载数据
  }
}
</script>

<style lang='scss' scoped>
.input-with-select .el-input-group__prepend {
  background-color: #0c6d97;
}
</style>
