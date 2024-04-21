import numpy as np
from wand.image import Image
import torch

def HWC3(x):
    assert x.dtype == np.uint8
    if x.ndim == 2:
        x = x[:, :, None]
    assert x.ndim == 3
    H, W, C = x.shape
    assert C == 1 or C == 3 or C == 4
    if C == 3:
        return x
    if C == 1:
        return np.concatenate([x, x, x], axis=2)
    if C == 4:
        color = x[:, :, 0:3].astype(np.float32)
        alpha = x[:, :, 3:4].astype(np.float32) / 255.0
        y = color * alpha + 255.0 * (1.0 - alpha)
        y = y.clip(0, 255).astype(np.uint8)
        return y

class Blur:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'radius': ('FLOAT', {'default': 0.0, 'min': 0, 'max': 100, 'step': 0.01}), 'sigma': ('FLOAT', {'default': 0.0, 'min': 0, 'max': 100, 'step': 0.01}), 'channel': (['undefined', 'red', 'gray', 'cyan', 'green', 'magenta', 'blue', 'yellow', 'black', 'alpha', 'opacity', 'index', 'readmask', 'write_mask', 'meta', 'composite_channels', 'all_channels', 'true_alpha', 'rgb', 'rgb_channels', 'gray_channels', 'sync_channels', 'default_channels'], {'default': 'rgb'})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"

    CATEGORY = "MagickWand"

    def execute(self, image, **kwargs):
        image_batch_np = image.cpu().detach().numpy().__mul__(255.).astype(np.uint8)
        out_images = []
        for image in image_batch_np:
            img_wand = Image.from_array(image)
            getattr(img_wand, 'blur')(**kwargs)
            out_images.append(HWC3(np.array(img_wand)))
        out_images = np.stack(out_images)
        out_images = torch.from_numpy(out_images.astype(np.float32) / 255.)
        return (out_images,)


class Canny:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'radius': ('FLOAT', {'default': 0.0, 'min': 0, 'max': 100, 'step': 0.01}), 'sigma': ('FLOAT', {'default': 1.0, 'min': 0, 'max': 100, 'step': 0.01}), 'lower_percent': ('FLOAT', {'default': 0.1, 'min': 0, 'max': 100, 'step': 0.01}), 'upper_percent': ('FLOAT', {'default': 0.3, 'min': 0, 'max': 100, 'step': 0.01})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"

    CATEGORY = "MagickWand"

    def execute(self, image, **kwargs):
        image_batch_np = image.cpu().detach().numpy().__mul__(255.).astype(np.uint8)
        out_images = []
        for image in image_batch_np:
            img_wand = Image.from_array(image)
            getattr(img_wand, 'canny')(**kwargs)
            out_images.append(HWC3(np.array(img_wand)))
        out_images = np.stack(out_images)
        out_images = torch.from_numpy(out_images.astype(np.float32) / 255.)
        return (out_images,)


class Charcoal:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'radius': ('FLOAT', {'default': 0, 'min': 0, 'max': 100, 'step': 0.01}), 'sigma': ('FLOAT', {'default': 0, 'min': 0, 'max': 100, 'step': 0.01})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"

    CATEGORY = "MagickWand"

    def execute(self, image, **kwargs):
        image_batch_np = image.cpu().detach().numpy().__mul__(255.).astype(np.uint8)
        out_images = []
        for image in image_batch_np:
            img_wand = Image.from_array(image)
            getattr(img_wand, 'charcoal')(**kwargs)
            out_images.append(HWC3(np.array(img_wand)))
        out_images = np.stack(out_images)
        out_images = torch.from_numpy(out_images.astype(np.float32) / 255.)
        return (out_images,)


class Chop:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'width': ('INT', {'default': 0, 'min': 0, 'max': 100}), 'height': ('INT', {'default': 0, 'min': 0, 'max': 100}), 'x': ('INT', {'default': 0, 'min': 0, 'max': 100}), 'y': ('INT', {'default': 0, 'min': 0, 'max': 100}), 'gravity': (['forget', 'north_west', 'north', 'north_east', 'west', 'center', 'east', 'south_west', 'south', 'south_east', 'static'], {'default': 'forget'})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"

    CATEGORY = "MagickWand"

    def execute(self, image, **kwargs):
        image_batch_np = image.cpu().detach().numpy().__mul__(255.).astype(np.uint8)
        out_images = []
        for image in image_batch_np:
            img_wand = Image.from_array(image)
            getattr(img_wand, 'chop')(**kwargs)
            out_images.append(HWC3(np.array(img_wand)))
        out_images = np.stack(out_images)
        out_images = torch.from_numpy(out_images.astype(np.float32) / 255.)
        return (out_images,)


class Clahe:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'width': ('INT', {'default': 0, 'min': 0, 'max': 100}), 'height': ('INT', {'default': 0, 'min': 0, 'max': 100}), 'number_bins': ('FLOAT', {'default': 0, 'min': 0, 'max': 100, 'step': 0.01}), 'clip_limit': ('FLOAT', {'default': 0, 'min': 0, 'max': 100, 'step': 0.01})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"

    CATEGORY = "MagickWand"

    def execute(self, image, **kwargs):
        image_batch_np = image.cpu().detach().numpy().__mul__(255.).astype(np.uint8)
        out_images = []
        for image in image_batch_np:
            img_wand = Image.from_array(image)
            getattr(img_wand, 'clahe')(**kwargs)
            out_images.append(HWC3(np.array(img_wand)))
        out_images = np.stack(out_images)
        out_images = torch.from_numpy(out_images.astype(np.float32) / 255.)
        return (out_images,)


class Clamp:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'channel': (['undefined', 'red', 'gray', 'cyan', 'green', 'magenta', 'blue', 'yellow', 'black', 'alpha', 'opacity', 'index', 'readmask', 'write_mask', 'meta', 'composite_channels', 'all_channels', 'true_alpha', 'rgb', 'rgb_channels', 'gray_channels', 'sync_channels', 'default_channels'], {'default': 'rgb'})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"

    CATEGORY = "MagickWand"

    def execute(self, image, **kwargs):
        image_batch_np = image.cpu().detach().numpy().__mul__(255.).astype(np.uint8)
        out_images = []
        for image in image_batch_np:
            img_wand = Image.from_array(image)
            getattr(img_wand, 'clamp')(**kwargs)
            out_images.append(HWC3(np.array(img_wand)))
        out_images = np.stack(out_images)
        out_images = torch.from_numpy(out_images.astype(np.float32) / 255.)
        return (out_images,)


class Combine:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'channel': (['undefined', 'red', 'gray', 'cyan', 'green', 'magenta', 'blue', 'yellow', 'black', 'alpha', 'opacity', 'index', 'readmask', 'write_mask', 'meta', 'composite_channels', 'all_channels', 'true_alpha', 'rgb', 'rgb_channels', 'gray_channels', 'sync_channels', 'default_channels'], {'default': 'rgb'}), 'colorspace': (['undefined', 'cmy', 'cmyk', 'gray', 'hcl', 'hclp', 'hsb', 'hsi', 'hsl', 'hsv', 'hwb', 'lab', 'lch', 'lchab', 'lchuv', 'log', 'lms', 'luv', 'ohta', 'rec601ycbcr', 'rec709ycbcr', 'rgb', 'scrgb', 'srgb', 'transparent', 'xyy', 'xyz', 'ycbcr', 'ycc', 'ydbdr', 'yiq', 'ypbpr', 'yuv'], {'default': 'undefined'})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"

    CATEGORY = "MagickWand"

    def execute(self, image, **kwargs):
        image_batch_np = image.cpu().detach().numpy().__mul__(255.).astype(np.uint8)
        out_images = []
        for image in image_batch_np:
            img_wand = Image.from_array(image)
            getattr(img_wand, 'combine')(**kwargs)
            out_images.append(HWC3(np.array(img_wand)))
        out_images = np.stack(out_images)
        out_images = torch.from_numpy(out_images.astype(np.float32) / 255.)
        return (out_images,)


class Complex:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'operator': (['undefined', 'add', 'conjugate', 'divide', 'magnitude', 'multiply', 'real_imaginary', 'subtract'], {'default': 'undefined'}), 'snr': ('STRING', {'multiline': False})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"

    CATEGORY = "MagickWand"

    def execute(self, image, **kwargs):
        image_batch_np = image.cpu().detach().numpy().__mul__(255.).astype(np.uint8)
        out_images = []
        for image in image_batch_np:
            img_wand = Image.from_array(image)
            getattr(img_wand, 'complex')(**kwargs)
            out_images.append(HWC3(np.array(img_wand)))
        out_images = np.stack(out_images)
        out_images = torch.from_numpy(out_images.astype(np.float32) / 255.)
        return (out_images,)


class Concat:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'stacked': ('BOOLEAN', {'default': False})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"

    CATEGORY = "MagickWand"

    def execute(self, image, **kwargs):
        image_batch_np = image.cpu().detach().numpy().__mul__(255.).astype(np.uint8)
        out_images = []
        for image in image_batch_np:
            img_wand = Image.from_array(image)
            getattr(img_wand, 'concat')(**kwargs)
            out_images.append(HWC3(np.array(img_wand)))
        out_images = np.stack(out_images)
        out_images = torch.from_numpy(out_images.astype(np.float32) / 255.)
        return (out_images,)


class Contrast:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'sharpen': ('BOOLEAN', {'default': True})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"

    CATEGORY = "MagickWand"

    def execute(self, image, **kwargs):
        image_batch_np = image.cpu().detach().numpy().__mul__(255.).astype(np.uint8)
        out_images = []
        for image in image_batch_np:
            img_wand = Image.from_array(image)
            getattr(img_wand, 'contrast')(**kwargs)
            out_images.append(HWC3(np.array(img_wand)))
        out_images = np.stack(out_images)
        out_images = torch.from_numpy(out_images.astype(np.float32) / 255.)
        return (out_images,)


class Crop:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'left': ('INT', {'default': 0, 'min': 0, 'max': 100}), 'top': ('INT', {'default': 0, 'min': 0, 'max': 100}), 'right': ('INT', {'default': 0, 'min': 0, 'max': 100}), 'bottom': ('INT', {'default': 0, 'min': 0, 'max': 100}), 'width': ('INT', {'default': 0, 'min': 0, 'max': 100}), 'height': ('INT', {'default': 0, 'min': 0, 'max': 100}), 'reset_coords': ('BOOLEAN', {'default': True}), 'gravity': (['forget', 'north_west', 'north', 'north_east', 'west', 'center', 'east', 'south_west', 'south', 'south_east', 'static'], {'default': 'forget'})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"

    CATEGORY = "MagickWand"

    def execute(self, image, **kwargs):
        image_batch_np = image.cpu().detach().numpy().__mul__(255.).astype(np.uint8)
        out_images = []
        for image in image_batch_np:
            img_wand = Image.from_array(image)
            getattr(img_wand, 'crop')(**kwargs)
            out_images.append(HWC3(np.array(img_wand)))
        out_images = np.stack(out_images)
        out_images = torch.from_numpy(out_images.astype(np.float32) / 255.)
        return (out_images,)


class Decipher:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'passphrase': ('STRING', {'multiline': False})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"

    CATEGORY = "MagickWand"

    def execute(self, image, **kwargs):
        image_batch_np = image.cpu().detach().numpy().__mul__(255.).astype(np.uint8)
        out_images = []
        for image in image_batch_np:
            img_wand = Image.from_array(image)
            getattr(img_wand, 'decipher')(**kwargs)
            out_images.append(HWC3(np.array(img_wand)))
        out_images = np.stack(out_images)
        out_images = torch.from_numpy(out_images.astype(np.float32) / 255.)
        return (out_images,)


class Deskew:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'threshold': ('FLOAT', {'default': 0, 'min': 0, 'max': 100, 'step': 0.01})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"

    CATEGORY = "MagickWand"

    def execute(self, image, **kwargs):
        image_batch_np = image.cpu().detach().numpy().__mul__(255.).astype(np.uint8)
        out_images = []
        for image in image_batch_np:
            img_wand = Image.from_array(image)
            getattr(img_wand, 'deskew')(**kwargs)
            out_images.append(HWC3(np.array(img_wand)))
        out_images = np.stack(out_images)
        out_images = torch.from_numpy(out_images.astype(np.float32) / 255.)
        return (out_images,)


class Distort:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'method': ('STRING', {'multiline': False}), 'arguments': ('STRING', {'multiline': False}), 'best_fit': ('BOOLEAN', {'default': False}), 'filter': (['undefined', 'point', 'box', 'triangle', 'hermite', 'hanning', 'hamming', 'blackman', 'gaussian', 'quadratic', 'cubic', 'catrom', 'mitchell', 'jinc', 'sinc', 'sincfast', 'kaiser', 'welsh', 'parzen', 'bohman', 'bartlett', 'lagrange', 'lanczos', 'lanczossharp', 'lanczos2', 'lanczos2sharp', 'robidoux', 'robidouxsharp', 'cosine', 'spline', 'sentinel'], {'default': 'undefined'})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"

    CATEGORY = "MagickWand"

    def execute(self, image, **kwargs):
        image_batch_np = image.cpu().detach().numpy().__mul__(255.).astype(np.uint8)
        out_images = []
        for image in image_batch_np:
            img_wand = Image.from_array(image)
            getattr(img_wand, 'distort')(**kwargs)
            out_images.append(HWC3(np.array(img_wand)))
        out_images = np.stack(out_images)
        out_images = torch.from_numpy(out_images.astype(np.float32) / 255.)
        return (out_images,)


class Edge:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'radius': ('FLOAT', {'default': 0.0, 'min': 0, 'max': 100, 'step': 0.01})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"

    CATEGORY = "MagickWand"

    def execute(self, image, **kwargs):
        image_batch_np = image.cpu().detach().numpy().__mul__(255.).astype(np.uint8)
        out_images = []
        for image in image_batch_np:
            img_wand = Image.from_array(image)
            getattr(img_wand, 'edge')(**kwargs)
            out_images.append(HWC3(np.array(img_wand)))
        out_images = np.stack(out_images)
        out_images = torch.from_numpy(out_images.astype(np.float32) / 255.)
        return (out_images,)


class Emboss:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'radius': ('FLOAT', {'default': 0.0, 'min': 0, 'max': 100, 'step': 0.01}), 'sigma': ('FLOAT', {'default': 0.0, 'min': 0, 'max': 100, 'step': 0.01})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"

    CATEGORY = "MagickWand"

    def execute(self, image, **kwargs):
        image_batch_np = image.cpu().detach().numpy().__mul__(255.).astype(np.uint8)
        out_images = []
        for image in image_batch_np:
            img_wand = Image.from_array(image)
            getattr(img_wand, 'emboss')(**kwargs)
            out_images.append(HWC3(np.array(img_wand)))
        out_images = np.stack(out_images)
        out_images = torch.from_numpy(out_images.astype(np.float32) / 255.)
        return (out_images,)


class Encipher:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'passphrase': ('STRING', {'multiline': False})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"

    CATEGORY = "MagickWand"

    def execute(self, image, **kwargs):
        image_batch_np = image.cpu().detach().numpy().__mul__(255.).astype(np.uint8)
        out_images = []
        for image in image_batch_np:
            img_wand = Image.from_array(image)
            getattr(img_wand, 'encipher')(**kwargs)
            out_images.append(HWC3(np.array(img_wand)))
        out_images = np.stack(out_images)
        out_images = torch.from_numpy(out_images.astype(np.float32) / 255.)
        return (out_images,)


class Equalize:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'channel': (['undefined', 'red', 'gray', 'cyan', 'green', 'magenta', 'blue', 'yellow', 'black', 'alpha', 'opacity', 'index', 'readmask', 'write_mask', 'meta', 'composite_channels', 'all_channels', 'true_alpha', 'rgb', 'rgb_channels', 'gray_channels', 'sync_channels', 'default_channels'], {'default': 'rgb'})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"

    CATEGORY = "MagickWand"

    def execute(self, image, **kwargs):
        image_batch_np = image.cpu().detach().numpy().__mul__(255.).astype(np.uint8)
        out_images = []
        for image in image_batch_np:
            img_wand = Image.from_array(image)
            getattr(img_wand, 'equalize')(**kwargs)
            out_images.append(HWC3(np.array(img_wand)))
        out_images = np.stack(out_images)
        out_images = torch.from_numpy(out_images.astype(np.float32) / 255.)
        return (out_images,)


class Evaluate:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'operator': (['undefined', 'abs', 'add', 'addmodulus', 'and', 'cosine', 'divide', 'exponential', 'gaussiannoise', 'impulsenoise', 'laplaciannoise', 'leftshift', 'log', 'max', 'mean', 'median', 'min', 'multiplicativenoise', 'multiply', 'or', 'poissonnoise', 'pow', 'rightshift', 'rootmeansquare', 'set', 'sine', 'subtract', 'sum', 'thresholdblack', 'threshold', 'thresholdwhite', 'uniformnoise', 'xor', 'inverse_log'], {'default': 'undefined'}), 'value': ('FLOAT', {'default': 0.0, 'min': 0, 'max': 100, 'step': 0.01}), 'channel': (['undefined', 'red', 'gray', 'cyan', 'green', 'magenta', 'blue', 'yellow', 'black', 'alpha', 'opacity', 'index', 'readmask', 'write_mask', 'meta', 'composite_channels', 'all_channels', 'true_alpha', 'rgb', 'rgb_channels', 'gray_channels', 'sync_channels', 'default_channels'], {'default': 'rgb'})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"

    CATEGORY = "MagickWand"

    def execute(self, image, **kwargs):
        image_batch_np = image.cpu().detach().numpy().__mul__(255.).astype(np.uint8)
        out_images = []
        for image in image_batch_np:
            img_wand = Image.from_array(image)
            getattr(img_wand, 'evaluate')(**kwargs)
            out_images.append(HWC3(np.array(img_wand)))
        out_images = np.stack(out_images)
        out_images = torch.from_numpy(out_images.astype(np.float32) / 255.)
        return (out_images,)


class Extent:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'width': ('INT', {'default': 0, 'min': 0, 'max': 100}), 'height': ('INT', {'default': 0, 'min': 0, 'max': 100}), 'x': ('INT', {'default': 0, 'min': 0, 'max': 100}), 'y': ('INT', {'default': 0, 'min': 0, 'max': 100}), 'gravity': (['forget', 'north_west', 'north', 'north_east', 'west', 'center', 'east', 'south_west', 'south', 'south_east', 'static'], {'default': 'forget'})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"

    CATEGORY = "MagickWand"

    def execute(self, image, **kwargs):
        image_batch_np = image.cpu().detach().numpy().__mul__(255.).astype(np.uint8)
        out_images = []
        for image in image_batch_np:
            img_wand = Image.from_array(image)
            getattr(img_wand, 'extent')(**kwargs)
            out_images.append(HWC3(np.array(img_wand)))
        out_images = np.stack(out_images)
        out_images = torch.from_numpy(out_images.astype(np.float32) / 255.)
        return (out_images,)


class Function:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'function': (['undefined', 'arcsin', 'arctan', 'polynomial', 'sinusoid'], {'default': 'undefined'}), 'arguments': ('STRING', {'multiline': False}), 'channel': (['undefined', 'red', 'gray', 'cyan', 'green', 'magenta', 'blue', 'yellow', 'black', 'alpha', 'opacity', 'index', 'readmask', 'write_mask', 'meta', 'composite_channels', 'all_channels', 'true_alpha', 'rgb', 'rgb_channels', 'gray_channels', 'sync_channels', 'default_channels'], {'default': 'rgb'})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"

    CATEGORY = "MagickWand"

    def execute(self, image, **kwargs):
        image_batch_np = image.cpu().detach().numpy().__mul__(255.).astype(np.uint8)
        out_images = []
        for image in image_batch_np:
            img_wand = Image.from_array(image)
            getattr(img_wand, 'function')(**kwargs)
            out_images.append(HWC3(np.array(img_wand)))
        out_images = np.stack(out_images)
        out_images = torch.from_numpy(out_images.astype(np.float32) / 255.)
        return (out_images,)


class Gamma:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'adjustment_value': ('FLOAT', {'default': 1.0, 'min': 0, 'max': 100, 'step': 0.01}), 'channel': (['undefined', 'red', 'gray', 'cyan', 'green', 'magenta', 'blue', 'yellow', 'black', 'alpha', 'opacity', 'index', 'readmask', 'write_mask', 'meta', 'composite_channels', 'all_channels', 'true_alpha', 'rgb', 'rgb_channels', 'gray_channels', 'sync_channels', 'default_channels'], {'default': 'rgb'})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"

    CATEGORY = "MagickWand"

    def execute(self, image, **kwargs):
        image_batch_np = image.cpu().detach().numpy().__mul__(255.).astype(np.uint8)
        out_images = []
        for image in image_batch_np:
            img_wand = Image.from_array(image)
            getattr(img_wand, 'gamma')(**kwargs)
            out_images.append(HWC3(np.array(img_wand)))
        out_images = np.stack(out_images)
        out_images = torch.from_numpy(out_images.astype(np.float32) / 255.)
        return (out_images,)


class Implode:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'amount': ('FLOAT', {'default': 0.0, 'min': 0, 'max': 100, 'step': 0.01}), 'method': (['undefined', 'average', 'average9', 'average16', 'background', 'bilinear', 'blend', 'catrom', 'integer', 'mesh', 'nearest', 'spline'], {'default': 'undefined'})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"

    CATEGORY = "MagickWand"

    def execute(self, image, **kwargs):
        image_batch_np = image.cpu().detach().numpy().__mul__(255.).astype(np.uint8)
        out_images = []
        for image in image_batch_np:
            img_wand = Image.from_array(image)
            getattr(img_wand, 'implode')(**kwargs)
            out_images.append(HWC3(np.array(img_wand)))
        out_images = np.stack(out_images)
        out_images = torch.from_numpy(out_images.astype(np.float32) / 255.)
        return (out_images,)


class Kmeans:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'number_colors': ('INT', {'default': 0, 'min': 0, 'max': 100}), 'max_iterations': ('INT', {'default': 100, 'min': 0, 'max': 100}), 'tolerance': ('FLOAT', {'default': 0.01, 'min': 0, 'max': 100, 'step': 0.01})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"

    CATEGORY = "MagickWand"

    def execute(self, image, **kwargs):
        image_batch_np = image.cpu().detach().numpy().__mul__(255.).astype(np.uint8)
        out_images = []
        for image in image_batch_np:
            img_wand = Image.from_array(image)
            getattr(img_wand, 'kmeans')(**kwargs)
            out_images.append(HWC3(np.array(img_wand)))
        out_images = np.stack(out_images)
        out_images = torch.from_numpy(out_images.astype(np.float32) / 255.)
        return (out_images,)


class Kuwahara:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'radius': ('FLOAT', {'default': 1.0, 'min': 0, 'max': 100, 'step': 0.01}), 'sigma': ('FLOAT', {'default': 0, 'min': 0, 'max': 100, 'step': 0.01})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"

    CATEGORY = "MagickWand"

    def execute(self, image, **kwargs):
        image_batch_np = image.cpu().detach().numpy().__mul__(255.).astype(np.uint8)
        out_images = []
        for image in image_batch_np:
            img_wand = Image.from_array(image)
            getattr(img_wand, 'kuwahara')(**kwargs)
            out_images.append(HWC3(np.array(img_wand)))
        out_images = np.stack(out_images)
        out_images = torch.from_numpy(out_images.astype(np.float32) / 255.)
        return (out_images,)


class Level:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'black': ('FLOAT', {'default': 0.0, 'min': 0, 'max': 100, 'step': 0.01}), 'white': ('FLOAT', {'default': 0, 'min': 0, 'max': 100, 'step': 0.01}), 'gamma': ('FLOAT', {'default': 1.0, 'min': 0, 'max': 100, 'step': 0.01}), 'channel': (['undefined', 'red', 'gray', 'cyan', 'green', 'magenta', 'blue', 'yellow', 'black', 'alpha', 'opacity', 'index', 'readmask', 'write_mask', 'meta', 'composite_channels', 'all_channels', 'true_alpha', 'rgb', 'rgb_channels', 'gray_channels', 'sync_channels', 'default_channels'], {'default': 'rgb'})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"

    CATEGORY = "MagickWand"

    def execute(self, image, **kwargs):
        image_batch_np = image.cpu().detach().numpy().__mul__(255.).astype(np.uint8)
        out_images = []
        for image in image_batch_np:
            img_wand = Image.from_array(image)
            getattr(img_wand, 'level')(**kwargs)
            out_images.append(HWC3(np.array(img_wand)))
        out_images = np.stack(out_images)
        out_images = torch.from_numpy(out_images.astype(np.float32) / 255.)
        return (out_images,)


class Levelize:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'black': ('FLOAT', {'default': 0.0, 'min': 0, 'max': 100, 'step': 0.01}), 'white': ('FLOAT', {'default': 0, 'min': 0, 'max': 100, 'step': 0.01}), 'gamma': ('FLOAT', {'default': 1.0, 'min': 0, 'max': 100, 'step': 0.01}), 'channel': (['undefined', 'red', 'gray', 'cyan', 'green', 'magenta', 'blue', 'yellow', 'black', 'alpha', 'opacity', 'index', 'readmask', 'write_mask', 'meta', 'composite_channels', 'all_channels', 'true_alpha', 'rgb', 'rgb_channels', 'gray_channels', 'sync_channels', 'default_channels'], {'default': 'rgb'})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"

    CATEGORY = "MagickWand"

    def execute(self, image, **kwargs):
        image_batch_np = image.cpu().detach().numpy().__mul__(255.).astype(np.uint8)
        out_images = []
        for image in image_batch_np:
            img_wand = Image.from_array(image)
            getattr(img_wand, 'levelize')(**kwargs)
            out_images.append(HWC3(np.array(img_wand)))
        out_images = np.stack(out_images)
        out_images = torch.from_numpy(out_images.astype(np.float32) / 255.)
        return (out_images,)


class Mode:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'width': ('INT', {'default': 0, 'min': 0, 'max': 100}), 'height': ('INT', {'default': 0, 'min': 0, 'max': 100})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"

    CATEGORY = "MagickWand"

    def execute(self, image, **kwargs):
        image_batch_np = image.cpu().detach().numpy().__mul__(255.).astype(np.uint8)
        out_images = []
        for image in image_batch_np:
            img_wand = Image.from_array(image)
            getattr(img_wand, 'mode')(**kwargs)
            out_images.append(HWC3(np.array(img_wand)))
        out_images = np.stack(out_images)
        out_images = torch.from_numpy(out_images.astype(np.float32) / 255.)
        return (out_images,)


class Modulate:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'brightness': ('FLOAT', {'default': 100.0, 'min': 0, 'max': 100, 'step': 0.01}), 'saturation': ('FLOAT', {'default': 100.0, 'min': 0, 'max': 100, 'step': 0.01}), 'hue': ('FLOAT', {'default': 100.0, 'min': 0, 'max': 100, 'step': 0.01})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"

    CATEGORY = "MagickWand"

    def execute(self, image, **kwargs):
        image_batch_np = image.cpu().detach().numpy().__mul__(255.).astype(np.uint8)
        out_images = []
        for image in image_batch_np:
            img_wand = Image.from_array(image)
            getattr(img_wand, 'modulate')(**kwargs)
            out_images.append(HWC3(np.array(img_wand)))
        out_images = np.stack(out_images)
        out_images = torch.from_numpy(out_images.astype(np.float32) / 255.)
        return (out_images,)


class Morphology:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'method': (['undefined', 'convolve', 'correlate', 'erode', 'dilate', 'erode_intensity', 'dilate_intensity', 'iterative_distance', 'open', 'close', 'open_intensity', 'close_intensity', 'smooth', 'edgein', 'edgeout', 'edge', 'tophat', 'bottom_hat', 'hit_and_miss', 'thinning', 'thicken', 'distance', 'voronoi'], {'default': 'undefined'}), 'kernel': (['undefined', 'unity', 'gaussian', 'dog', 'log', 'blur', 'comet', 'binomial', 'laplacian', 'sobel', 'frei_chen', 'roberts', 'prewitt', 'compass', 'kirsch', 'diamond', 'square', 'rectangle', 'octagon', 'disk', 'plus', 'cross', 'ring', 'peaks', 'edges', 'corners', 'diagonals', 'line_ends', 'line_junctions', 'ridges', 'convex_hull', 'thin_se', 'skeleton', 'chebyshev', 'manhattan', 'octagonal', 'euclidean', 'user_defined'], {'default': 'undefined'}), 'iterations': ('INT', {'default': 1, 'min': 0, 'max': 100}), 'channel': (['undefined', 'red', 'gray', 'cyan', 'green', 'magenta', 'blue', 'yellow', 'black', 'alpha', 'opacity', 'index', 'readmask', 'write_mask', 'meta', 'composite_channels', 'all_channels', 'true_alpha', 'rgb', 'rgb_channels', 'gray_channels', 'sync_channels', 'default_channels'], {'default': 'rgb'})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"

    CATEGORY = "MagickWand"

    def execute(self, image, **kwargs):
        image_batch_np = image.cpu().detach().numpy().__mul__(255.).astype(np.uint8)
        out_images = []
        for image in image_batch_np:
            img_wand = Image.from_array(image)
            getattr(img_wand, 'morphology')(**kwargs)
            out_images.append(HWC3(np.array(img_wand)))
        out_images = np.stack(out_images)
        out_images = torch.from_numpy(out_images.astype(np.float32) / 255.)
        return (out_images,)


class Negate:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'grayscale': ('BOOLEAN', {'default': False}), 'channel': (['undefined', 'red', 'gray', 'cyan', 'green', 'magenta', 'blue', 'yellow', 'black', 'alpha', 'opacity', 'index', 'readmask', 'write_mask', 'meta', 'composite_channels', 'all_channels', 'true_alpha', 'rgb', 'rgb_channels', 'gray_channels', 'sync_channels', 'default_channels'], {'default': 'rgb'})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"

    CATEGORY = "MagickWand"

    def execute(self, image, **kwargs):
        image_batch_np = image.cpu().detach().numpy().__mul__(255.).astype(np.uint8)
        out_images = []
        for image in image_batch_np:
            img_wand = Image.from_array(image)
            getattr(img_wand, 'negate')(**kwargs)
            out_images.append(HWC3(np.array(img_wand)))
        out_images = np.stack(out_images)
        out_images = torch.from_numpy(out_images.astype(np.float32) / 255.)
        return (out_images,)


class Noise:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'noise_type': (['undefined', 'uniform', 'gaussian', 'multiplicative_gaussian', 'impulse', 'laplacian', 'poisson', 'random'], {'default': 'undefined'}), 'attenuate': ('FLOAT', {'default': 1.0, 'min': 0, 'max': 100, 'step': 0.01}), 'channel': (['undefined', 'red', 'gray', 'cyan', 'green', 'magenta', 'blue', 'yellow', 'black', 'alpha', 'opacity', 'index', 'readmask', 'write_mask', 'meta', 'composite_channels', 'all_channels', 'true_alpha', 'rgb', 'rgb_channels', 'gray_channels', 'sync_channels', 'default_channels'], {'default': 'rgb'})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"

    CATEGORY = "MagickWand"

    def execute(self, image, **kwargs):
        image_batch_np = image.cpu().detach().numpy().__mul__(255.).astype(np.uint8)
        out_images = []
        for image in image_batch_np:
            img_wand = Image.from_array(image)
            getattr(img_wand, 'noise')(**kwargs)
            out_images.append(HWC3(np.array(img_wand)))
        out_images = np.stack(out_images)
        out_images = torch.from_numpy(out_images.astype(np.float32) / 255.)
        return (out_images,)


class Normalize:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'channel': (['undefined', 'red', 'gray', 'cyan', 'green', 'magenta', 'blue', 'yellow', 'black', 'alpha', 'opacity', 'index', 'readmask', 'write_mask', 'meta', 'composite_channels', 'all_channels', 'true_alpha', 'rgb', 'rgb_channels', 'gray_channels', 'sync_channels', 'default_channels'], {'default': 'rgb'})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"

    CATEGORY = "MagickWand"

    def execute(self, image, **kwargs):
        image_batch_np = image.cpu().detach().numpy().__mul__(255.).astype(np.uint8)
        out_images = []
        for image in image_batch_np:
            img_wand = Image.from_array(image)
            getattr(img_wand, 'normalize')(**kwargs)
            out_images.append(HWC3(np.array(img_wand)))
        out_images = np.stack(out_images)
        out_images = torch.from_numpy(out_images.astype(np.float32) / 255.)
        return (out_images,)


class Polynomial:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'arguments': ('STRING', {'multiline': False})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"

    CATEGORY = "MagickWand"

    def execute(self, image, **kwargs):
        image_batch_np = image.cpu().detach().numpy().__mul__(255.).astype(np.uint8)
        out_images = []
        for image in image_batch_np:
            img_wand = Image.from_array(image)
            getattr(img_wand, 'polynomial')(**kwargs)
            out_images.append(HWC3(np.array(img_wand)))
        out_images = np.stack(out_images)
        out_images = torch.from_numpy(out_images.astype(np.float32) / 255.)
        return (out_images,)


class Posterize:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'levels': ('INT', {'default': 0, 'min': 0, 'max': 100}), 'dither': (['undefined', 'no', 'riemersma', 'floyd_steinberg'], {'default': 'undefined'})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"

    CATEGORY = "MagickWand"

    def execute(self, image, **kwargs):
        image_batch_np = image.cpu().detach().numpy().__mul__(255.).astype(np.uint8)
        out_images = []
        for image in image_batch_np:
            img_wand = Image.from_array(image)
            getattr(img_wand, 'posterize')(**kwargs)
            out_images.append(HWC3(np.array(img_wand)))
        out_images = np.stack(out_images)
        out_images = torch.from_numpy(out_images.astype(np.float32) / 255.)
        return (out_images,)


class Pseudo:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'width': ('INT', {'default': 0, 'min': 0, 'max': 100}), 'height': ('INT', {'default': 0, 'min': 0, 'max': 100}), 'pseudo': ('STRING', {'multiline': False})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"

    CATEGORY = "MagickWand"

    def execute(self, image, **kwargs):
        image_batch_np = image.cpu().detach().numpy().__mul__(255.).astype(np.uint8)
        out_images = []
        for image in image_batch_np:
            img_wand = Image.from_array(image)
            getattr(img_wand, 'pseudo')(**kwargs)
            out_images.append(HWC3(np.array(img_wand)))
        out_images = np.stack(out_images)
        out_images = torch.from_numpy(out_images.astype(np.float32) / 255.)
        return (out_images,)


class Quantize:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'number_colors': ('INT', {'default': 0, 'min': 0, 'max': 100}), 'colorspace_type': (['undefined', 'cmy', 'cmyk', 'gray', 'hcl', 'hclp', 'hsb', 'hsi', 'hsl', 'hsv', 'hwb', 'lab', 'lch', 'lchab', 'lchuv', 'log', 'lms', 'luv', 'ohta', 'rec601ycbcr', 'rec709ycbcr', 'rgb', 'scrgb', 'srgb', 'transparent', 'xyy', 'xyz', 'ycbcr', 'ycc', 'ydbdr', 'yiq', 'ypbpr', 'yuv'], {'default': 'undefined'}), 'treedepth': ('INT', {'default': 0, 'min': 0, 'max': 100}), 'dither': (['undefined', 'no', 'riemersma', 'floyd_steinberg'], {'default': 'undefined'}), 'measure_error': ('BOOLEAN', {'default': False})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"

    CATEGORY = "MagickWand"

    def execute(self, image, **kwargs):
        image_batch_np = image.cpu().detach().numpy().__mul__(255.).astype(np.uint8)
        out_images = []
        for image in image_batch_np:
            img_wand = Image.from_array(image)
            getattr(img_wand, 'quantize')(**kwargs)
            out_images.append(HWC3(np.array(img_wand)))
        out_images = np.stack(out_images)
        out_images = torch.from_numpy(out_images.astype(np.float32) / 255.)
        return (out_images,)


class Resample:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'x_res': ('FLOAT', {'default': 0, 'min': 0, 'max': 100, 'step': 0.01}), 'y_res': ('FLOAT', {'default': 0, 'min': 0, 'max': 100, 'step': 0.01}), 'filter': (['undefined', 'point', 'box', 'triangle', 'hermite', 'hanning', 'hamming', 'blackman', 'gaussian', 'quadratic', 'cubic', 'catrom', 'mitchell', 'jinc', 'sinc', 'sincfast', 'kaiser', 'welsh', 'parzen', 'bohman', 'bartlett', 'lagrange', 'lanczos', 'lanczossharp', 'lanczos2', 'lanczos2sharp', 'robidoux', 'robidouxsharp', 'cosine', 'spline', 'sentinel'], {'default': 'undefined'}), 'blur': ('FLOAT', {'default': 1, 'min': 0, 'max': 100, 'step': 0.01})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"

    CATEGORY = "MagickWand"

    def execute(self, image, **kwargs):
        image_batch_np = image.cpu().detach().numpy().__mul__(255.).astype(np.uint8)
        out_images = []
        for image in image_batch_np:
            img_wand = Image.from_array(image)
            getattr(img_wand, 'resample')(**kwargs)
            out_images.append(HWC3(np.array(img_wand)))
        out_images = np.stack(out_images)
        out_images = torch.from_numpy(out_images.astype(np.float32) / 255.)
        return (out_images,)


class Resize:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'width': ('INT', {'default': 0, 'min': 0, 'max': 100}), 'height': ('INT', {'default': 0, 'min': 0, 'max': 100}), 'filter': (['undefined', 'point', 'box', 'triangle', 'hermite', 'hanning', 'hamming', 'blackman', 'gaussian', 'quadratic', 'cubic', 'catrom', 'mitchell', 'jinc', 'sinc', 'sincfast', 'kaiser', 'welsh', 'parzen', 'bohman', 'bartlett', 'lagrange', 'lanczos', 'lanczossharp', 'lanczos2', 'lanczos2sharp', 'robidoux', 'robidouxsharp', 'cosine', 'spline', 'sentinel'], {'default': 'undefined'}), 'blur': ('FLOAT', {'default': 1, 'min': 0, 'max': 100, 'step': 0.01})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"

    CATEGORY = "MagickWand"

    def execute(self, image, **kwargs):
        image_batch_np = image.cpu().detach().numpy().__mul__(255.).astype(np.uint8)
        out_images = []
        for image in image_batch_np:
            img_wand = Image.from_array(image)
            getattr(img_wand, 'resize')(**kwargs)
            out_images.append(HWC3(np.array(img_wand)))
        out_images = np.stack(out_images)
        out_images = torch.from_numpy(out_images.astype(np.float32) / 255.)
        return (out_images,)


class Roll:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'x': ('INT', {'default': 0, 'min': 0, 'max': 100}), 'y': ('INT', {'default': 0, 'min': 0, 'max': 100})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"

    CATEGORY = "MagickWand"

    def execute(self, image, **kwargs):
        image_batch_np = image.cpu().detach().numpy().__mul__(255.).astype(np.uint8)
        out_images = []
        for image in image_batch_np:
            img_wand = Image.from_array(image)
            getattr(img_wand, 'roll')(**kwargs)
            out_images.append(HWC3(np.array(img_wand)))
        out_images = np.stack(out_images)
        out_images = torch.from_numpy(out_images.astype(np.float32) / 255.)
        return (out_images,)


class Sample:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'width': ('INT', {'default': 0, 'min': 0, 'max': 100}), 'height': ('INT', {'default': 0, 'min': 0, 'max': 100})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"

    CATEGORY = "MagickWand"

    def execute(self, image, **kwargs):
        image_batch_np = image.cpu().detach().numpy().__mul__(255.).astype(np.uint8)
        out_images = []
        for image in image_batch_np:
            img_wand = Image.from_array(image)
            getattr(img_wand, 'sample')(**kwargs)
            out_images.append(HWC3(np.array(img_wand)))
        out_images = np.stack(out_images)
        out_images = torch.from_numpy(out_images.astype(np.float32) / 255.)
        return (out_images,)


class Scale:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'columns': ('INT', {'default': 1, 'min': 0, 'max': 100}), 'rows': ('INT', {'default': 1, 'min': 0, 'max': 100})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"

    CATEGORY = "MagickWand"

    def execute(self, image, **kwargs):
        image_batch_np = image.cpu().detach().numpy().__mul__(255.).astype(np.uint8)
        out_images = []
        for image in image_batch_np:
            img_wand = Image.from_array(image)
            getattr(img_wand, 'scale')(**kwargs)
            out_images.append(HWC3(np.array(img_wand)))
        out_images = np.stack(out_images)
        out_images = torch.from_numpy(out_images.astype(np.float32) / 255.)
        return (out_images,)


class Shade:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'gray': ('BOOLEAN', {'default': False}), 'azimuth': ('FLOAT', {'default': 0.0, 'min': 0, 'max': 100, 'step': 0.01}), 'elevation': ('FLOAT', {'default': 0.0, 'min': 0, 'max': 100, 'step': 0.01})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"

    CATEGORY = "MagickWand"

    def execute(self, image, **kwargs):
        image_batch_np = image.cpu().detach().numpy().__mul__(255.).astype(np.uint8)
        out_images = []
        for image in image_batch_np:
            img_wand = Image.from_array(image)
            getattr(img_wand, 'shade')(**kwargs)
            out_images.append(HWC3(np.array(img_wand)))
        out_images = np.stack(out_images)
        out_images = torch.from_numpy(out_images.astype(np.float32) / 255.)
        return (out_images,)


class Shadow:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'alpha': ('FLOAT', {'default': 0.0, 'min': 0, 'max': 100, 'step': 0.01}), 'sigma': ('FLOAT', {'default': 0.0, 'min': 0, 'max': 100, 'step': 0.01}), 'x': ('INT', {'default': 0, 'min': 0, 'max': 100}), 'y': ('INT', {'default': 0, 'min': 0, 'max': 100})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"

    CATEGORY = "MagickWand"

    def execute(self, image, **kwargs):
        image_batch_np = image.cpu().detach().numpy().__mul__(255.).astype(np.uint8)
        out_images = []
        for image in image_batch_np:
            img_wand = Image.from_array(image)
            getattr(img_wand, 'shadow')(**kwargs)
            out_images.append(HWC3(np.array(img_wand)))
        out_images = np.stack(out_images)
        out_images = torch.from_numpy(out_images.astype(np.float32) / 255.)
        return (out_images,)


class Sharpen:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'radius': ('FLOAT', {'default': 0.0, 'min': 0, 'max': 100, 'step': 0.01}), 'sigma': ('FLOAT', {'default': 0.0, 'min': 0, 'max': 100, 'step': 0.01}), 'channel': (['undefined', 'red', 'gray', 'cyan', 'green', 'magenta', 'blue', 'yellow', 'black', 'alpha', 'opacity', 'index', 'readmask', 'write_mask', 'meta', 'composite_channels', 'all_channels', 'true_alpha', 'rgb', 'rgb_channels', 'gray_channels', 'sync_channels', 'default_channels'], {'default': 'rgb'})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"

    CATEGORY = "MagickWand"

    def execute(self, image, **kwargs):
        image_batch_np = image.cpu().detach().numpy().__mul__(255.).astype(np.uint8)
        out_images = []
        for image in image_batch_np:
            img_wand = Image.from_array(image)
            getattr(img_wand, 'sharpen')(**kwargs)
            out_images.append(HWC3(np.array(img_wand)))
        out_images = np.stack(out_images)
        out_images = torch.from_numpy(out_images.astype(np.float32) / 255.)
        return (out_images,)


class Shave:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'columns': ('INT', {'default': 0, 'min': 0, 'max': 100}), 'rows': ('INT', {'default': 0, 'min': 0, 'max': 100})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"

    CATEGORY = "MagickWand"

    def execute(self, image, **kwargs):
        image_batch_np = image.cpu().detach().numpy().__mul__(255.).astype(np.uint8)
        out_images = []
        for image in image_batch_np:
            img_wand = Image.from_array(image)
            getattr(img_wand, 'shave')(**kwargs)
            out_images.append(HWC3(np.array(img_wand)))
        out_images = np.stack(out_images)
        out_images = torch.from_numpy(out_images.astype(np.float32) / 255.)
        return (out_images,)


class Sketch:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'radius': ('FLOAT', {'default': 0.0, 'min': 0, 'max': 100, 'step': 0.01}), 'sigma': ('FLOAT', {'default': 0.0, 'min': 0, 'max': 100, 'step': 0.01}), 'angle': ('FLOAT', {'default': 0.0, 'min': 0, 'max': 100, 'step': 0.01})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"

    CATEGORY = "MagickWand"

    def execute(self, image, **kwargs):
        image_batch_np = image.cpu().detach().numpy().__mul__(255.).astype(np.uint8)
        out_images = []
        for image in image_batch_np:
            img_wand = Image.from_array(image)
            getattr(img_wand, 'sketch')(**kwargs)
            out_images.append(HWC3(np.array(img_wand)))
        out_images = np.stack(out_images)
        out_images = torch.from_numpy(out_images.astype(np.float32) / 255.)
        return (out_images,)


class Smush:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'stacked': ('BOOLEAN', {'default': False}), 'offset': ('INT', {'default': 0, 'min': 0, 'max': 100})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"

    CATEGORY = "MagickWand"

    def execute(self, image, **kwargs):
        image_batch_np = image.cpu().detach().numpy().__mul__(255.).astype(np.uint8)
        out_images = []
        for image in image_batch_np:
            img_wand = Image.from_array(image)
            getattr(img_wand, 'smush')(**kwargs)
            out_images.append(HWC3(np.array(img_wand)))
        out_images = np.stack(out_images)
        out_images = torch.from_numpy(out_images.astype(np.float32) / 255.)
        return (out_images,)


class Solarize:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'threshold': ('FLOAT', {'default': 0.0, 'min': 0, 'max': 100, 'step': 0.01}), 'channel': (['undefined', 'red', 'gray', 'cyan', 'green', 'magenta', 'blue', 'yellow', 'black', 'alpha', 'opacity', 'index', 'readmask', 'write_mask', 'meta', 'composite_channels', 'all_channels', 'true_alpha', 'rgb', 'rgb_channels', 'gray_channels', 'sync_channels', 'default_channels'], {'default': 'rgb'})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"

    CATEGORY = "MagickWand"

    def execute(self, image, **kwargs):
        image_batch_np = image.cpu().detach().numpy().__mul__(255.).astype(np.uint8)
        out_images = []
        for image in image_batch_np:
            img_wand = Image.from_array(image)
            getattr(img_wand, 'solarize')(**kwargs)
            out_images.append(HWC3(np.array(img_wand)))
        out_images = np.stack(out_images)
        out_images = torch.from_numpy(out_images.astype(np.float32) / 255.)
        return (out_images,)


class Splice:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'width': ('INT', {'default': 0, 'min': 0, 'max': 100}), 'height': ('INT', {'default': 0, 'min': 0, 'max': 100}), 'x': ('INT', {'default': 0, 'min': 0, 'max': 100}), 'y': ('INT', {'default': 0, 'min': 0, 'max': 100})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"

    CATEGORY = "MagickWand"

    def execute(self, image, **kwargs):
        image_batch_np = image.cpu().detach().numpy().__mul__(255.).astype(np.uint8)
        out_images = []
        for image in image_batch_np:
            img_wand = Image.from_array(image)
            getattr(img_wand, 'splice')(**kwargs)
            out_images.append(HWC3(np.array(img_wand)))
        out_images = np.stack(out_images)
        out_images = torch.from_numpy(out_images.astype(np.float32) / 255.)
        return (out_images,)


class Spread:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'radius': ('FLOAT', {'default': 0.0, 'min': 0, 'max': 100, 'step': 0.01}), 'method': (['undefined', 'average', 'average9', 'average16', 'background', 'bilinear', 'blend', 'catrom', 'integer', 'mesh', 'nearest', 'spline'], {'default': 'undefined'})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"

    CATEGORY = "MagickWand"

    def execute(self, image, **kwargs):
        image_batch_np = image.cpu().detach().numpy().__mul__(255.).astype(np.uint8)
        out_images = []
        for image in image_batch_np:
            img_wand = Image.from_array(image)
            getattr(img_wand, 'spread')(**kwargs)
            out_images.append(HWC3(np.array(img_wand)))
        out_images = np.stack(out_images)
        out_images = torch.from_numpy(out_images.astype(np.float32) / 255.)
        return (out_images,)


class Statistic:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'stat': (['undefined', 'gradient', 'maximum', 'mean', 'median', 'minimum', 'mode', 'nonpeak', 'root_mean_square', 'standard_deviation'], {'default': 'undefined'}), 'width': ('INT', {'default': 0, 'min': 0, 'max': 100}), 'height': ('INT', {'default': 0, 'min': 0, 'max': 100}), 'channel': (['undefined', 'red', 'gray', 'cyan', 'green', 'magenta', 'blue', 'yellow', 'black', 'alpha', 'opacity', 'index', 'readmask', 'write_mask', 'meta', 'composite_channels', 'all_channels', 'true_alpha', 'rgb', 'rgb_channels', 'gray_channels', 'sync_channels', 'default_channels'], {'default': 'rgb'})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"

    CATEGORY = "MagickWand"

    def execute(self, image, **kwargs):
        image_batch_np = image.cpu().detach().numpy().__mul__(255.).astype(np.uint8)
        out_images = []
        for image in image_batch_np:
            img_wand = Image.from_array(image)
            getattr(img_wand, 'statistic')(**kwargs)
            out_images.append(HWC3(np.array(img_wand)))
        out_images = np.stack(out_images)
        out_images = torch.from_numpy(out_images.astype(np.float32) / 255.)
        return (out_images,)


class Swirl:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'degree': ('FLOAT', {'default': 0.0, 'min': 0, 'max': 100, 'step': 0.01}), 'method': (['undefined', 'average', 'average9', 'average16', 'background', 'bilinear', 'blend', 'catrom', 'integer', 'mesh', 'nearest', 'spline'], {'default': 'undefined'})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"

    CATEGORY = "MagickWand"

    def execute(self, image, **kwargs):
        image_batch_np = image.cpu().detach().numpy().__mul__(255.).astype(np.uint8)
        out_images = []
        for image in image_batch_np:
            img_wand = Image.from_array(image)
            getattr(img_wand, 'swirl')(**kwargs)
            out_images.append(HWC3(np.array(img_wand)))
        out_images = np.stack(out_images)
        out_images = torch.from_numpy(out_images.astype(np.float32) / 255.)
        return (out_images,)


class Threshold:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'threshold': ('FLOAT', {'default': 0.5, 'min': 0, 'max': 100, 'step': 0.01}), 'channel': (['undefined', 'red', 'gray', 'cyan', 'green', 'magenta', 'blue', 'yellow', 'black', 'alpha', 'opacity', 'index', 'readmask', 'write_mask', 'meta', 'composite_channels', 'all_channels', 'true_alpha', 'rgb', 'rgb_channels', 'gray_channels', 'sync_channels', 'default_channels'], {'default': 'rgb'})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"

    CATEGORY = "MagickWand"

    def execute(self, image, **kwargs):
        image_batch_np = image.cpu().detach().numpy().__mul__(255.).astype(np.uint8)
        out_images = []
        for image in image_batch_np:
            img_wand = Image.from_array(image)
            getattr(img_wand, 'threshold')(**kwargs)
            out_images.append(HWC3(np.array(img_wand)))
        out_images = np.stack(out_images)
        out_images = torch.from_numpy(out_images.astype(np.float32) / 255.)
        return (out_images,)


class Thumbnail:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'width': ('INT', {'default': 0, 'min': 0, 'max': 100}), 'height': ('INT', {'default': 0, 'min': 0, 'max': 100})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"

    CATEGORY = "MagickWand"

    def execute(self, image, **kwargs):
        image_batch_np = image.cpu().detach().numpy().__mul__(255.).astype(np.uint8)
        out_images = []
        for image in image_batch_np:
            img_wand = Image.from_array(image)
            getattr(img_wand, 'thumbnail')(**kwargs)
            out_images.append(HWC3(np.array(img_wand)))
        out_images = np.stack(out_images)
        out_images = torch.from_numpy(out_images.astype(np.float32) / 255.)
        return (out_images,)


class Transform:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'crop': ('STRING', {'multiline': False}), 'resize': ('STRING', {'multiline': False})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"

    CATEGORY = "MagickWand"

    def execute(self, image, **kwargs):
        image_batch_np = image.cpu().detach().numpy().__mul__(255.).astype(np.uint8)
        out_images = []
        for image in image_batch_np:
            img_wand = Image.from_array(image)
            getattr(img_wand, 'transform')(**kwargs)
            out_images.append(HWC3(np.array(img_wand)))
        out_images = np.stack(out_images)
        out_images = torch.from_numpy(out_images.astype(np.float32) / 255.)
        return (out_images,)


class Transparentize:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'transparency': ('FLOAT', {'default': 0, 'min': 0, 'max': 100, 'step': 0.01})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"

    CATEGORY = "MagickWand"

    def execute(self, image, **kwargs):
        image_batch_np = image.cpu().detach().numpy().__mul__(255.).astype(np.uint8)
        out_images = []
        for image in image_batch_np:
            img_wand = Image.from_array(image)
            getattr(img_wand, 'transparentize')(**kwargs)
            out_images.append(HWC3(np.array(img_wand)))
        out_images = np.stack(out_images)
        out_images = torch.from_numpy(out_images.astype(np.float32) / 255.)
        return (out_images,)


class Vignette:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'radius': ('FLOAT', {'default': 0.0, 'min': 0, 'max': 100, 'step': 0.01}), 'sigma': ('FLOAT', {'default': 0.0, 'min': 0, 'max': 100, 'step': 0.01}), 'x': ('INT', {'default': 0, 'min': 0, 'max': 100}), 'y': ('INT', {'default': 0, 'min': 0, 'max': 100})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"

    CATEGORY = "MagickWand"

    def execute(self, image, **kwargs):
        image_batch_np = image.cpu().detach().numpy().__mul__(255.).astype(np.uint8)
        out_images = []
        for image in image_batch_np:
            img_wand = Image.from_array(image)
            getattr(img_wand, 'vignette')(**kwargs)
            out_images.append(HWC3(np.array(img_wand)))
        out_images = np.stack(out_images)
        out_images = torch.from_numpy(out_images.astype(np.float32) / 255.)
        return (out_images,)


class Wave:
    @classmethod
    def INPUT_TYPES(s):
        return {'required': {'image': ('IMAGE',), 'amplitude': ('FLOAT', {'default': 0.0, 'min': 0, 'max': 100, 'step': 0.01}), 'wave_length': ('FLOAT', {'default': 0.0, 'min': 0, 'max': 100, 'step': 0.01}), 'method': (['undefined', 'average', 'average9', 'average16', 'background', 'bilinear', 'blend', 'catrom', 'integer', 'mesh', 'nearest', 'spline'], {'default': 'undefined'})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "execute"

    CATEGORY = "MagickWand"

    def execute(self, image, **kwargs):
        image_batch_np = image.cpu().detach().numpy().__mul__(255.).astype(np.uint8)
        out_images = []
        for image in image_batch_np:
            img_wand = Image.from_array(image)
            getattr(img_wand, 'wave')(**kwargs)
            out_images.append(HWC3(np.array(img_wand)))
        out_images = np.stack(out_images)
        out_images = torch.from_numpy(out_images.astype(np.float32) / 255.)
        return (out_images,)

NODE_CLASS_MAPPINGS = {
    "ImageMagick Blur": Blur,
    "ImageMagick Canny": Canny,
    "ImageMagick Charcoal": Charcoal,
    "ImageMagick Chop": Chop,
    "ImageMagick Clahe": Clahe,
    "ImageMagick Clamp": Clamp,
    "ImageMagick Combine": Combine,
    "ImageMagick Complex": Complex,
    "ImageMagick Concat": Concat,
    "ImageMagick Contrast": Contrast,
    "ImageMagick Crop": Crop,
    "ImageMagick Decipher": Decipher,
    "ImageMagick Deskew": Deskew,
    "ImageMagick Distort": Distort,
    "ImageMagick Edge": Edge,
    "ImageMagick Emboss": Emboss,
    "ImageMagick Encipher": Encipher,
    "ImageMagick Equalize": Equalize,
    "ImageMagick Evaluate": Evaluate,
    "ImageMagick Extent": Extent,
    "ImageMagick Function": Function,
    "ImageMagick Gamma": Gamma,
    "ImageMagick Implode": Implode,
    "ImageMagick Kmeans": Kmeans,
    "ImageMagick Kuwahara": Kuwahara,
    "ImageMagick Level": Level,
    "ImageMagick Levelize": Levelize,
    "ImageMagick Mode": Mode,
    "ImageMagick Modulate": Modulate,
    "ImageMagick Morphology": Morphology,
    "ImageMagick Negate": Negate,
    "ImageMagick Noise": Noise,
    "ImageMagick Normalize": Normalize,
    "ImageMagick Polynomial": Polynomial,
    "ImageMagick Posterize": Posterize,
    "ImageMagick Pseudo": Pseudo,
    "ImageMagick Quantize": Quantize,
    "ImageMagick Resample": Resample,
    "ImageMagick Resize": Resize,
    "ImageMagick Roll": Roll,
    "ImageMagick Sample": Sample,
    "ImageMagick Scale": Scale,
    "ImageMagick Shade": Shade,
    "ImageMagick Shadow": Shadow,
    "ImageMagick Sharpen": Sharpen,
    "ImageMagick Shave": Shave,
    "ImageMagick Sketch": Sketch,
    "ImageMagick Smush": Smush,
    "ImageMagick Solarize": Solarize,
    "ImageMagick Splice": Splice,
    "ImageMagick Spread": Spread,
    "ImageMagick Statistic": Statistic,
    "ImageMagick Swirl": Swirl,
    "ImageMagick Threshold": Threshold,
    "ImageMagick Thumbnail": Thumbnail,
    "ImageMagick Transform": Transform,
    "ImageMagick Transparentize": Transparentize,
    "ImageMagick Vignette": Vignette,
    "ImageMagick Wave": Wave,
}
