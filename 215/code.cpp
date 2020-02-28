#include <vector>
#include <algorithm>

using std::vector;
using std::iter_swap;

class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        quickSort(nums);
        
        return nums[nums.size() - k];
    }
    
private:
    void quickSort(vector<int>& nums)
    {
        sort(nums, 0, nums.size() - 1);
    }
    
    void sort(vector<int>& nums, int lo, int li)
    {
        if (lo >= li)
            return;
        
        int j = partition(nums, lo, li);
        
        sort(nums, lo, j);
        sort(nums, j + 1, li);
    }
    
    int partition(vector<int>& nums, int lo, int li)
    {
        int i = lo, j = li + 1;
        int v = nums[lo];
        
        while(true)
        {
            while(nums[++i] > v)
            {
                if (i == li)
                    break;
            }
            
            while(nums[--j] < v)
            {
                if (j == lo)
                    break;
            }
            
            if (i >= j)
                break;
            
            iter_swap(nums.begin() + i, nums.begin() + j);
        }
        
        iter_swap(nums.begin() + lo, nums.begin() + j);
        
        return j;
    }
};


int main()
{
    vector<int> a { 3, 2, 1, 5, 6, 4 };

    Solution s;

    s.findKthLargest(a, 2);
}