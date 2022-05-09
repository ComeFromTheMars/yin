<template>
  <div class="gContainer">
    <gSearch @getData="update" />
    <!-- <threeGraph /> -->
    <threeGraph
      :data="data"
      :names="names"
      :labels="labels"
      :linkTypes="linkTypes"
    />
  </div>
</template>

<script>
// @ is an alias to /src
import gSearch from '@/components/gSearch.vue'
import threeGraph from '@/components/threeGraph.vue'
import axios from 'axios'
export default {
  name: 'threeView',
  components: {
    gSearch,
    threeGraph
  },
  data () {
    return {
      // d3jsonParser()处理 json 后返回的结果
      data: {
        nodes: [],
        links: []
      },
      names: ['普通节点', '终端节点', '中转节点', '匿名节点', '地标节点'],
      labels: ['1', '2', '3', '4'],
      linkTypes: ['', 'type', 'locate', 'export']
    }
  },
  methods: {
    // 视图更新
    update (json) {
      if (Object.keys(json).length === 0) {
        axios.get('http://localhost:5000/').then(
          response => {
            this.d3jsonParser(response.data)
          }
        ).catch(
          error => {
            console.log(error.message)
          }
        )
      } else {
        axios.get('http://localhost:5000/match', {
          params: {
            ip: json
          }
        }).then(
          response => {
            if (Object.keys(response.data[0]).length !== 0) {
              this.data = response.data
              console.log(this.data)
              this.d3jsonParser(this.data)
            } else {
              alert('没有匹配到节点和关系！！！！')
            }
          }
        ).catch(
          error => {
            console.log(error.message)
          }
        )
      }
    },
    /*eslint-disable*/
    // 解析json数据，主要负责数据的去重、标准化
    d3jsonParser (json) {
      const nodes =[]
      const links = [] // 存放节点和关系
      const nodeSet = [] // 存放去重后nodes的id
      for (let item of json) {
        for (let segment of item.p.segments) {
          // 重新更改data格式
          if (nodeSet.indexOf(segment.start.identity) == -1) {
            nodeSet.push(segment.start.identity)
            nodes.push({
              id: segment.start.identity,
              label: segment.start.labels[0],
              properties: segment.start.properties
            })
          }
          if (nodeSet.indexOf(segment.end.identity) == -1) {
            nodeSet.push(segment.end.identity)
            nodes.push({
              id: segment.end.identity,
              label: segment.end.labels[0],
              properties: segment.end.properties
            })
          }

          links.push({
            source: segment.relationship.start,
            target: segment.relationship.end,
            type: segment.relationship.type,
            properties: segment.relationship.properties
          })
        }
      }
      this.data = { nodes, links }
    },
    d3jsonParser1(json){
      const nodes =[]
      const links = [] // 存放节点和关系
      const nodeSet = [] // 存放去重后nodes的id
      for (let item of json) {
        for (let segment of item.p.segments) {
          // 重新更改data格式
          if (nodeSet.indexOf(segment.start.identity) == -1) {
            nodeSet.push(segment.start.identity)
            nodes.push({
              id: segment.start.identity,
              label: segment.start.labels[0],
              properties: segment.start.properties
            })
          }
        }
      }
      this.data = { nodes, links }
    }
  }
}
</script>

<style lang="scss" scoped>
.gContainer {
  position: relative;
  border: 2px #000 solid;
  background-color: #030202;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  overflow: hidden;
}
</style>
