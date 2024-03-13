PREFIX ?= /usr

all:
	@echo RUN \'make install\' to install LiberFetch
	@echo RUN \'make uninstall\' to remove LiberFetch

install:
	@mkdir -p $(PREFIX)/local/share/lfetch{,/colors,/main_module,/system_info,/window_manager}

	@install -Dm755 colors/colors.py $(DESTDIR)$(PREFIX)/local/share/lfetch/colors/colors.py
	@install -Dm755 main_module/main_module.py $(DESTDIR)$(PREFIX)/local/share/lfetch/main_module/main_module.py
	@install -Dm755 system_info/system_info.py $(DESTDIR)$(PREFIX)/local/share/lfetch/system_info/system_info.py
	@install -Dm755 window_manager/window_manager.py $(DESTDIR)$(PREFIX)/local/share/lfetch/window_manager/window_manager.py
	@install -Dm755 lfetch $(DESTDIR)$(PREFIX)/bin/lfetch

uninstall:
	@rm -r $(DESTDIR)$(PREFIX)/local/share/lfetch
	@rm -f $(DESTDIR)$(PREFIX)/bin/lfetch
