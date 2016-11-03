import time


class Benchmark(object):
    """Benchmarking methods"""
    @staticmethod
    def run_tests(method, iter=10):
        tests = Tests()
        times = []
        for i in range(iter):
            print "Running iteration %s of %s for %s" % ((i + 1), iter, method)
            start = time.time()
            eval("tests."+method+"()")
            end = time.time()
            secs = end - start
            msecs = secs * 1000  # millisecs
            times.append(msecs)
        result = {}
        result.update({'times': times})
        total = 0
        for i_time in times:
            total = total + i_time
        avg = total / iter
        result.update({'avg': avg})
        return result

    @staticmethod
    def compare_tests(first, second, iter=10):
        first_r     = Benchmark.run_tests(first,iter)
        second_r    = Benchmark.run_tests(second, iter)
        difference  = second_r['avg']-first_r['avg']

        print "%s: %s" % (first, first_r['avg'])
        print "%s: %s" % (second, second_r['avg'])
        print "%s is %s faster than %s" % (first, difference, second)

        return difference


class Tests(object):
    def __init__(self):
        from zp_old.core.image import Image
        self.img    = Image()
        self.file   = 'kosovo.jpg'

    def hash_with_path(self):
        value = self.file
        self.img.p_hash(value)
        self.img.d_hash(value)
        self.img.w_hash(value)

    def hash_with_object(self):
        value = self.img.open_image(self.file)
        self.img.p_hash(value)
        self.img.d_hash(value)
        self.img.w_hash(value)

    def thumb_path(self):
        value = self.file
        self.img.large_thumb(value)
        self.img.medium_thumb(value)
        self.img.small_thumb(value)

    def thumb_object(self):
        value = self.img.open_image(self.file)
        self.img.large_thumb(value)
        self.img.medium_thumb(value)
        self.img.small_thumb(value)
        value.close()