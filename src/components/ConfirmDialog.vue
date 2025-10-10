<template>
  <div class="modal-overlay" v-if="props.visible" @click="handleOverlayClick">
    <div class="modal-container" @click.stop>
      <h2 class="modal-title">{{ props.title }}</h2>
      
      <p class="modal-message">{{ props.message }}</p>
      
      <div class="button-group">
        <button class="btn confirm-btn" @click="confirm">
          {{ props.confirmText || '确认' }}
        </button>
        <button class="btn cancel-btn" @click="cancel">
          {{ props.cancelText || '取消' }}
        </button>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
// 定义props
const props = defineProps<{
  visible: boolean;
  title: string;
  message: string;
  confirmText?: string;
  cancelText?: string;
}>();

// 定义emit
const emit = defineEmits<{
  (e: 'close'): void;
  (e: 'confirm'): void;
}>();

// 确认操作
const confirm = () => {
  emit('confirm');
  emit('close');
};

// 取消操作
const cancel = () => {
  emit('close');
};

// 点击遮罩层关闭
const handleOverlayClick = () => {
  if (props.visible) {
    emit('close');
  }
};
</script>

<style scoped>
.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-color: rgba(0, 0, 0, 0.5);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 1000;
}

.modal-container {
  background-color: white;
  border-radius: 8px;
  padding: 24px;
  width: 90%;
  max-width: 400px;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
}

.modal-title {
  font-size: 18px;
  font-weight: bold;
  margin-bottom: 12px;
  text-align: center;
}

.modal-message {
  font-size: 14px;
  color: #333;
  text-align: center;
  margin-bottom: 20px;
  line-height: 1.5;
}

.button-group {
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.btn {
  padding: 10px 16px;
  border: none;
  border-radius: 4px;
  font-size: 14px;
  cursor: pointer;
  transition: background-color 0.2s;
}

.confirm-btn {
  background-color: black;
  color: white;
}

.confirm-btn:hover {
  background-color: #333;
}

.cancel-btn {
  background-color: #f5f5f5;
  color: #333;
}

.cancel-btn:hover {
  background-color: #e0e0e0;
}
</style>