# import heapq

# class Solution:
#     def kthSmallestProduct(self, nums1: List[int], nums2: List[int], k: int) -> int:
        # products=[]
        # for num1 in nums1:
        #     product=[]
        #     for num2 in nums2:
        #         product.append(num1*num2)
        #     if num1<0:
        #         product=product[::-1]
        #     products.append(product)

        # heap=[(lst.pop(0),i) for i,lst in enumerate(products)]
        # heapq.heapify(heap)
        # for i in range(k):
        #     item,listnum=heapq.heappop(heap)
        #     if products[listnum]:
        #         heapq.heappush(heap,(products[listnum].pop(0),listnum))

        # return item

class Solution:
    def f(self, nums2: List[int], x1: int, v: int) -> int:
        if x1 > 0:
            return bisect_right(nums2, v // x1)
        elif x1 < 0:
            return len(nums2) - bisect_left(nums2, -(-v // x1))
        else:
            return len(nums2) if v >= 0 else 0

    def kthSmallestProduct(
        self, nums1: List[int], nums2: List[int], k: int) -> int:
        n1 = len(nums1)
        left, right = -(10**10), 10**10
        while left <= right:
            mid = (left + right) // 2
            count = 0
            for i in range(n1):
                count += self.f(nums2, nums1[i], mid)
            if count < k:
                left = mid + 1
            else:
                right = mid - 1
        return left