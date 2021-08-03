#include <vector>

using namespace std;
/*快速排序
1、每次递归分区中，变量i记录着从左边开始第一个大于pivot的数值位置；
2、变量j始终在i的右侧，只要j位置的数值小于pivot，就将i、j位置上的数据交换；
*/

class Solution {
    int partition(vector<int>& nums, int left, int right) { // 快速排序 C++
        int pivot = nums[right]; // 选一个数值作为pivot
        int i = left - 1;
        for (int j = left; j <= right - 1; j++) { // 将数组中的数值按照选中的pivot大小进行划分，小于等于的在一起，大于的在一起
            if (nums[j] <= pivot) {
                i = i + 1;
                swap(nums[i], nums[j]); // 交换位置
            }
        }
        swap(nums[i + 1], nums[right]); // 这一行代码的意义是：把一开始就搁置的pivot再拉回来，放回中间的位置。左边是小于等于的元素，右边是大于的。
        return i + 1; // 输出pivot位置
    }
    void quicksort(vector<int>& nums, int left, int right) {
        if (left < right) { // 快速排序
            int pos = partition(nums, left, right);
            quicksort(nums, left, pos - 1);
            quicksort(nums, pos + 1, right);
        }
    }
public:
    vector<int> sortArray(vector<int>& nums) {
        quicksort(nums, 0, (int)nums.size() - 1);
        return nums;
    }
};

