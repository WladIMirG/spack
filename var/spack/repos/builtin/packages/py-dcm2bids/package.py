# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyDcm2bids(PythonPackage):
    """Reorganising NIfTI files from dcm2niix into the Brain Imaging Data
    Structure."""

    homepage = "https://github.com/unfmontreal/Dcm2Bids"
    pypi = "dcm2bids/dcm2bids-2.1.9.tar.gz"

    version("2.1.9", sha256="d962bd0a7f1ed200ecb699e8ddb29ff58f09ab2f850a7f37511b79c62189f715")

    depends_on("python@3.7:", type=("build", "run"))
    depends_on("py-setuptools", type="build")
    depends_on("py-setuptools-scm", type="build")

    depends_on("py-future@0.17.1:", type=("build", "run"))
    depends_on("dcm2niix", type=("build", "run"))
