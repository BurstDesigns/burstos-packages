spec ?= $(error spec=<package>/<package>.spec is required)
outdir ?= $(CURDIR)/out

srpm:
	dnf -y install rpmdevtools rpm-build
	spectool -g -C "$(outdir)" "$(spec)"
	if [ -x "$(dir $(spec))sources.sh" ]; then "$(dir $(spec))sources.sh" "$(spec)" "$(outdir)"; fi
	rpmbuild -bs --define "_sourcedir $(outdir)" --define "_srcrpmdir $(outdir)" "$(spec)"
